"""
Authentication helpers for password hashing and session-based auth.
"""

import os
from typing import Optional
from fastapi import Request
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from app.models.base import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    """Hash a plain password using bcrypt."""
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Validate a plain password against its hash."""
    if not hashed_password:
        return False
    return pwd_context.verify(plain_password, hashed_password)


def set_session_user(request: Request, user: User) -> None:
    """Persist the logged-in user in the signed session cookie."""
    request.session["user_id"] = user.id
    request.session["user_email"] = user.email


def clear_session(request: Request) -> None:
    """Remove user data from the session."""
    request.session.pop("user_id", None)
    request.session.pop("user_email", None)
    request.session.pop("oauth_state", None)


def get_current_user(request: Request, db: Session) -> Optional[User]:
    """Fetch the current user from the DB using the session."""
    user_id = request.session.get("user_id")
    if not user_id:
        return None
    user = db.query(User).filter(User.id == user_id, User.is_member.is_(True)).first()
    return user
