"""
Tamsui Church Shao-nian Management System
Main application entry point
"""

import os

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware
from pathlib import Path

# Import routers
from app.routers import home, record, devotion, profile, auth
from app.database import SessionLocal
from app.models.base import User

# Initialize FastAPI app
app = FastAPI(
    title="Tamsui Church Shao-nian System",
    description="教會青年聚會管理系統",
    version="0.1.0",
)

# Session middleware for signed cookies
app.add_middleware(
    SessionMiddleware,
    secret_key=os.getenv("SECRET_KEY", "change-me"),
    session_cookie="ts_session",
    https_only=False,
)

# Mount static files
static_dir = Path(__file__).parent / "static"
if static_dir.exists():
    app.mount("/static", StaticFiles(directory=static_dir), name="static")

# Set up templates
templates_dir = Path(__file__).parent / "templates"
templates = Jinja2Templates(directory=str(templates_dir))

# Include routers (no prefix for page routes)
app.include_router(home.router, tags=["home"])
app.include_router(record.router, tags=["record"])
app.include_router(devotion.router, tags=["devotion"])
app.include_router(profile.router, tags=["profile"])
app.include_router(auth.router, tags=["auth"])


# Simple membership gate: redirect unauthenticated visitors to the login page
PUBLIC_PATHS = {
    "/login",
    "/auth/google",
    "/auth/google/callback",
    "/health",
}
STATIC_PREFIXES = ["/static"]


@app.middleware("http")
async def require_login(request, call_next):
    path = request.url.path
    if (
        path in PUBLIC_PATHS
        or path.startswith("/auth/")
        or any(path.startswith(prefix) for prefix in STATIC_PREFIXES)
    ):
        return await call_next(request)

    user_id = request.session.get("user_id")
    if not user_id:
        return RedirectResponse("/login", status_code=303)

    db = SessionLocal()
    try:
        user = db.query(User).filter(User.id == user_id, User.is_member.is_(True)).first()
        if not user:
            request.session.clear()
            return RedirectResponse("/login", status_code=303)
        request.state.user = user
        response = await call_next(request)
        return response
    finally:
        db.close()


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "ok", "service": "Tamsui Church Shao-nian System"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
