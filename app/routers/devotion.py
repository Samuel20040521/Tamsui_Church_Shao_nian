"""
Devotion (靈修) router
"""

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path
from datetime import datetime

router = APIRouter()

# Set up templates
templates_dir = Path(__file__).parent.parent / "templates"
templates = Jinja2Templates(directory=str(templates_dir))


@router.get("/devotion", response_class=HTMLResponse)
async def get_devotion(request: Request):
    """
    Render devotion page with dummy content
    """
    # Dummy devotion data
    devotion_data = {
        "date": datetime.now().strftime("%Y年%m月%d日"),
        "video_title": "JAM 愛的影響力 - 每日靈修 (模擬)",
        "verse": {
            "text": "神愛世人，甚至將他的獨生子賜給他們，叫一切信他的，不至滅亡，反得永生。",
            "reference": "約翰福音 3:16",
        },
        "user_note": "",
    }

    return templates.TemplateResponse(
        "devotion.html",
        {
            "request": request,
            "active_tab": "devotion",
            "devotion": devotion_data,
        },
    )
