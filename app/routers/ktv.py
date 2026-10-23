"""
KTV (點歌) router
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db

router = APIRouter()


@router.get("/ktv/songs")
async def get_song_list(
    search: str = None, skip: int = 0, limit: int = 50, db: Session = Depends(get_db)
):
    """
    Get KTV song list with optional search
    """
    return {"total": 0, "songs": []}


@router.post("/ktv/request")
async def request_song(
    song_id: int, requester_id: int = None, db: Session = Depends(get_db)
):
    """
    Request a song to be added to queue
    Requester ID optional for anonymous requests
    """
    return {"success": True, "queue_id": 1, "position": 1}


@router.get("/ktv/queue")
async def get_queue(db: Session = Depends(get_db)):
    """
    Get current KTV queue
    """
    return {"queue": [], "current_song": None, "next_songs": []}


@router.delete("/ktv/queue/{queue_id}")
async def remove_from_queue(queue_id: int, db: Session = Depends(get_db)):
    """
    Remove song from queue
    Admin only
    """
    return {"success": True, "queue_id": queue_id}


@router.post("/ktv/queue/{queue_id}/play")
async def mark_as_played(queue_id: int, db: Session = Depends(get_db)):
    """
    Mark queue item as played
    Admin only
    """
    return {"success": True, "queue_id": queue_id}


@router.put("/ktv/queue/reorder")
async def reorder_queue(order: list, db: Session = Depends(get_db)):
    """
    Reorder KTV queue
    Admin only
    """
    return {"success": True, "message": "Queue reordered"}
