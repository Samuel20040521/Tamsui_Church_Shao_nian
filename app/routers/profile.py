"""
Profile (個人) router
"""

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path

router = APIRouter()

# Set up templates
templates_dir = Path(__file__).parent.parent / "templates"
templates = Jinja2Templates(directory=str(templates_dir))


@router.get("/profile", response_class=HTMLResponse)
async def get_profile(request: Request):
    """
    Render profile page with dummy user data
    """
    # Dummy user profile data
    user = {
        "email": "leader@example.com",
        "nickname": "冠宇",
        "nicknames": ["冠宇", "冠冠", "GU"],
        "avatar_url": "",
        "bio": "熱愛敬拜與牧養，喜歡陪伴每一位弟兄姊妹。",
        "position": "會長",
        "birthday": "2002-05-10",
    }

    # Dummy roster of 20 users with required attributes
    users = [
        {
            "name": "張天恩",
            "position": "輔導",
            "nickname": "張天恩",
            "birthday": "1990-03-12",
        },
        {
            "name": "李以琳",
            "position": "輔導",
            "nickname": "李以琳",
            "birthday": "1991-07-28",
        },
        {
            "name": "陳冠宇",
            "position": "會長",
            "nickname": "陳冠宇",
            "birthday": "2002-05-10",
        },
        {
            "name": "林家禾",
            "position": "活動",
            "nickname": "林家禾",
            "birthday": "2003-02-18",
        },
        {
            "name": "周子安",
            "position": "小組長",
            "nickname": "周子安",
            "birthday": "2001-11-02",
        },
        {
            "name": "許雅雯",
            "position": "小組長",
            "nickname": "許雅雯",
            "birthday": "2000-09-23",
        },
        {
            "name": "王柏翰",
            "position": "文書",
            "nickname": "王柏翰",
            "birthday": "2002-12-30",
        },
        {
            "name": "吳亭瑜",
            "position": "總務",
            "nickname": "吳亭瑜",
            "birthday": "2001-04-15",
        },
        {
            "name": "蔡品妤",
            "position": "契友",
            "nickname": "蔡品妤",
            "birthday": "2003-08-08",
        },
        {
            "name": "黃敬恩",
            "position": "契友",
            "nickname": "黃敬恩",
            "birthday": "2004-01-19",
        },
        {
            "name": "何紹庭",
            "position": "契友",
            "nickname": "何紹庭",
            "birthday": "2002-06-05",
        },
        {
            "name": "吳思穎",
            "position": "契友",
            "nickname": "吳思穎",
            "birthday": "2003-10-27",
        },
        {
            "name": "趙怡君",
            "position": "契友",
            "nickname": "趙怡君",
            "birthday": "2000-07-14",
        },
        {
            "name": "江冠廷",
            "position": "契友",
            "nickname": "江冠廷",
            "birthday": "2001-03-09",
        },
        {
            "name": "邱以諾",
            "position": "契友",
            "nickname": "邱以諾",
            "birthday": "2002-02-22",
        },
        {
            "name": "徐宥辰",
            "position": "契友",
            "nickname": "徐宥辰",
            "birthday": "2001-05-25",
        },
        {
            "name": "張雅筑",
            "position": "契友",
            "nickname": "張雅筑",
            "birthday": "2003-12-12",
        },
        {
            "name": "李承勳",
            "position": "契友",
            "nickname": "李承勳",
            "birthday": "2004-04-03",
        },
        {
            "name": "林沛恩",
            "position": "契友",
            "nickname": "林沛恩",
            "birthday": "2002-09-30",
        },
        {
            "name": "高子鈞",
            "position": "契友",
            "nickname": "高子鈞",
            "birthday": "2000-08-17",
        },
    ]

    # Dummy Google bindings
    google_accounts = [
        {"id": 1, "email": "user1@gmail.com", "name": "張小明"},
        {"id": 2, "email": "user2@gmail.com", "name": "張大明"},
    ]

    return templates.TemplateResponse(
        "profile.html",
        {
            "request": request,
            "active_tab": "profile",
            "user": user,
            "users": users,
            "google_accounts": google_accounts,
        },
    )
