"""
Attendance (點名) router
"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db

router = APIRouter()


@router.post("/attendance/nfc-checkin/{gathering_id}")
async def nfc_checkin(gathering_id: int, nfc_code: str, db: Session = Depends(get_db)):
    """
    NFC card check-in
    Marks user as attended
    """
    return {"success": True, "gathering_id": gathering_id, "status": "checked_in"}


@router.post("/attendance/qr-checkin/{gathering_id}")
async def qr_checkin(gathering_id: int, qr_code: str, db: Session = Depends(get_db)):
    """
    Dynamic QR code check-in
    QR code expires after 10 seconds
    """
    return {"success": True, "gathering_id": gathering_id, "status": "checked_in"}


@router.get("/attendance/{gathering_id}")
async def get_attendance_list(gathering_id: int, db: Session = Depends(get_db)):
    """
    Get attendance list for a gathering
    Admin/Leader only
    """
    return {"gathering_id": gathering_id, "attendance_records": []}


@router.put("/attendance/{attendance_id}")
async def update_attendance_record(
    attendance_id: int, status: str, notes: str = None, db: Session = Depends(get_db)
):
    """
    Update attendance record manually
    Admin/Leader only
    """
    return {"success": True, "attendance_id": attendance_id}


@router.get("/attendance/statistics/{gathering_id}")
async def get_attendance_statistics(gathering_id: int, db: Session = Depends(get_db)):
    """
    Get attendance statistics for a gathering
    """
    return {
        "gathering_id": gathering_id,
        "total_users": 0,
        "attended": 0,
        "not_attended": 0,
        "pending": 0,
        "attendance_rate": 0.0,
    }
