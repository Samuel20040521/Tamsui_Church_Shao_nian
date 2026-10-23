"""
Record (聚會紀錄) router
"""

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path

router = APIRouter()

# Set up templates
templates_dir = Path(__file__).parent.parent / "templates"
templates = Jinja2Templates(directory=str(templates_dir))


@router.get("/record", response_class=HTMLResponse)
async def get_records(request: Request):
    """
    Render record page with dummy past gatherings
    """
    # Dummy past gatherings data (newest to oldest)
    records = [
        {
            "id": 1,
            "title": "感恩節特別聚會",
            "date": "2024年11月24日",
            "image_placeholder": True,
        },
        {
            "id": 2,
            "title": "青年敬拜之夜",
            "date": "2024年11月17日",
            "image_placeholder": True,
        },
        {
            "id": 3,
            "title": "主日聚會",
            "date": "2024年11月10日",
            "image_placeholder": True,
        },
        {
            "id": 4,
            "title": "小組分享會",
            "date": "2024年11月3日",
            "image_placeholder": True,
        },
    ]

    return templates.TemplateResponse(
        "record.html",
        {
            "request": request,
            "active_tab": "record",
            "records": records,
        },
    )
