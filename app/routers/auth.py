"""
Authentication routes for email/password and Google OAuth.
"""

import os
import secrets
from typing import Optional
from pathlib import Path
from urllib.parse import urlencode

from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from google_auth_oauthlib.flow import Flow
from google.oauth2 import id_token
from google.auth.transport import requests as grequests
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.base import User, UserGoogleBinding
from app.utils.auth import verify_password, set_session_user, clear_session

router = APIRouter()

templates_dir = Path(__file__).parent.parent / "templates"
templates = Jinja2Templates(directory=str(templates_dir))

GOOGLE_SCOPES = [
    "https://www.googleapis.com/auth/userinfo.email",
    "https://www.googleapis.com/auth/userinfo.profile",
    "openid",
]
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
GOOGLE_REDIRECT_URI = os.getenv(
    "GOOGLE_REDIRECT_URI", "http://localhost:8000/auth/google/callback"
)


def _google_flow(state: Optional[str] = None) -> Flow:
    """Create a Google OAuth Flow from env configuration."""
    return Flow.from_client_config(
        {
            "web": {
                "client_id": GOOGLE_CLIENT_ID or "",
                "client_secret": GOOGLE_CLIENT_SECRET or "",
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token",
                "redirect_uris": [GOOGLE_REDIRECT_URI],
            }
        },
        scopes=GOOGLE_SCOPES,
        state=state,
        redirect_uri=GOOGLE_REDIRECT_URI,
    )


@router.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    """Render the login page with optional error messages."""
    error = request.query_params.get("error")
    return templates.TemplateResponse(
        "login.html",
        {"request": request, "hide_nav": True, "error": error},
    )


@router.post("/login")
async def login_with_password(
    request: Request,
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db),
):
    """Authenticate using email/password stored on the User record."""
    user = db.query(User).filter(User.email == email).first()
    if not user or not user.is_member:
        params = urlencode({"error": "帳號不存在或未啟用"})
        return RedirectResponse(f"/login?{params}", status_code=303)

    if not user.password_hash or not verify_password(password, user.password_hash):
        params = urlencode({"error": "密碼錯誤，請再試一次"})
        return RedirectResponse(f"/login?{params}", status_code=303)

    set_session_user(request, user)
    return RedirectResponse("/", status_code=303)


@router.get("/logout")
async def logout(request: Request):
    """Clear session and redirect to login."""
    clear_session(request)
    return RedirectResponse("/login", status_code=303)


@router.get("/auth/google")
async def login_with_google(request: Request):
    """Kick off the Google OAuth flow."""
    if not GOOGLE_CLIENT_ID or not GOOGLE_CLIENT_SECRET:
        params = urlencode({"error": "請先在環境變數設定 Google OAuth 資訊"})
        return RedirectResponse(f"/login?{params}", status_code=303)

    state = secrets.token_urlsafe(16)
    request.session["oauth_state"] = state
    flow = _google_flow(state)
    authorization_url, _ = flow.authorization_url(
        access_type="offline",
        include_granted_scopes="true",
        prompt="consent",
    )
    return RedirectResponse(authorization_url)


@router.get("/auth/google/callback")
async def google_callback(request: Request, db: Session = Depends(get_db)):
    """Handle Google OAuth callback and log the user in if recognized as a member."""
    stored_state = request.session.get("oauth_state")
    incoming_state = request.query_params.get("state")
    if not stored_state or stored_state != incoming_state:
        params = urlencode({"error": "登入流程逾時，請再試一次"})
        clear_session(request)
        return RedirectResponse(f"/login?{params}", status_code=303)

    try:
        flow = _google_flow(incoming_state)
        flow.fetch_token(authorization_response=str(request.url))
        credentials = flow.credentials
        idinfo = id_token.verify_oauth2_token(
            credentials.id_token, grequests.Request(), GOOGLE_CLIENT_ID
        )
        email = idinfo.get("email")
        google_id = idinfo.get("sub")
        name = idinfo.get("name")
        picture = idinfo.get("picture")
    except Exception:
        params = urlencode({"error": "Google 登入失敗，請再試一次"})
        return RedirectResponse(f"/login?{params}", status_code=303)
    finally:
        request.session.pop("oauth_state", None)

    if not email or not google_id:
        params = urlencode({"error": "無法取得 Google 帳號資訊"})
        return RedirectResponse(f"/login?{params}", status_code=303)

    user = db.query(User).filter(User.email == email, User.is_member.is_(True)).first()
    if not user:
        params = urlencode({"error": "此 Google 帳號未在成員名單中"})
        return RedirectResponse(f"/login?{params}", status_code=303)

    binding = (
        db.query(UserGoogleBinding)
        .filter(
            UserGoogleBinding.user_id == user.id,
            UserGoogleBinding.google_id == google_id,
        )
        .first()
    )
    if not binding:
        binding = UserGoogleBinding(
            user_id=user.id,
            google_id=google_id,
            email=email,
            name=name,
            picture_url=picture,
        )
        db.add(binding)
    else:
        binding.email = email
        binding.name = name
        binding.picture_url = picture

    db.commit()

    set_session_user(request, user)
    return RedirectResponse("/", status_code=303)
