"""
Home page router
"""

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path

router = APIRouter()

# Set up templates
templates_dir = Path(__file__).parent.parent / "templates"
templates = Jinja2Templates(directory=str(templates_dir))


@router.get("/", response_class=HTMLResponse)
async def get_home(request: Request):
    """
    Render home page with dummy data
    """
    # Dummy data for gathering
    gathering = {
        "title": "主日聚會",
        "date": "2024年12月8日 10:00",
        "location": "教會",
        "main_speaker": "王牧師",
        "moderator": "李弟兄",
        "pianist": "張姊妹",
    }

    # Dummy TODO items
    todos = [
        {"id": 1, "title": "準備主日講道", "completed": False},
        {"id": 2, "title": "確認聚會場地", "completed": True},
        {"id": 3, "title": "聯繫新朋友", "completed": False},
    ]

    return templates.TemplateResponse(
        "home.html",
        {
            "request": request,
            "active_tab": "home",
            "gathering": gathering,
            "todos": todos,
        },
    )
