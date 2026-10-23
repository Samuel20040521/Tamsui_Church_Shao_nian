"""
Pydantic schemas for request/response validation
"""

from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime
from enum import Enum


class AttendanceStatusSchema(str, Enum):
    """Attendance status"""

    ATTEND = "attend"
    NOT_ATTEND = "not_attend"
    PENDING = "pending"


# User Schemas
class UserProfileCreate(BaseModel):
    """User profile creation"""

    nickname: Optional[str] = None
    avatar_url: Optional[str] = None
    bio: Optional[str] = None


class UserProfileResponse(BaseModel):
    """User profile response"""

    id: int
    nickname: Optional[str]
    avatar_url: Optional[str]
    bio: Optional[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class UserGoogleBindingResponse(BaseModel):
    """Google binding response"""

    id: int
    google_id: str
    email: str
    name: str
    picture_url: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True


class UserResponse(BaseModel):
    """User response"""

    id: int
    email: str
    phone: Optional[str]
    is_admin: bool
    is_leader: bool
    profile: Optional[UserProfileResponse]
    google_bindings: List[UserGoogleBindingResponse] = []
    created_at: datetime

    class Config:
        from_attributes = True


# Gathering Schemas
class GatheringCreate(BaseModel):
    """Gathering creation"""

    title: str
    date: datetime
    location: Optional[str] = None
    main_speaker: Optional[str] = None
    moderator: Optional[str] = None
    pianist: Optional[str] = None
    description: Optional[str] = None


class GatheringUpdate(BaseModel):
    """Gathering update"""

    title: Optional[str] = None
    date: Optional[datetime] = None
    location: Optional[str] = None
    main_speaker: Optional[str] = None
    moderator: Optional[str] = None
    pianist: Optional[str] = None
    description: Optional[str] = None


class GatheringResponse(BaseModel):
    """Gathering response"""

    id: int
    title: str
    date: datetime
    location: Optional[str]
    main_speaker: Optional[str]
    moderator: Optional[str]
    pianist: Optional[str]
    description: Optional[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# Attendance Schemas
class AttendanceUpdate(BaseModel):
    """Attendance update"""

    status: AttendanceStatusSchema
    notes: Optional[str] = None


class AttendanceResponse(BaseModel):
    """Attendance response"""

    id: int
    gathering_id: int
    user_id: int
    status: AttendanceStatusSchema
    check_in_time: Optional[datetime]
    notes: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True


# Record Schemas
class RecordPostCreate(BaseModel):
    """Record post creation"""

    gathering_id: int
    title: str
    content: Optional[str] = None
    image_url: Optional[str] = None


class RecordPostUpdate(BaseModel):
    """Record post update"""

    title: Optional[str] = None
    content: Optional[str] = None
    image_url: Optional[str] = None


class RecordCommentCreate(BaseModel):
    """Record comment creation"""

    content: str


class RecordLikeCreate(BaseModel):
    """Record like creation"""

    pass


class RecordCommentResponse(BaseModel):
    """Record comment response"""

    id: int
    content: str
    created_at: datetime

    class Config:
        from_attributes = True


class RecordPostResponse(BaseModel):
    """Record post response"""

    id: int
    gathering_id: int
    title: str
    content: Optional[str]
    image_url: Optional[str]
    created_at: datetime
    updated_at: datetime
    comments: List[RecordCommentResponse] = []
    like_count: int = 0

    class Config:
        from_attributes = True


# Devotion Schemas
class DevotionVideoResponse(BaseModel):
    """Devotion video response"""

    id: int
    youtube_id: str
    title: str
    description: Optional[str]
    thumbnail_url: Optional[str]
    video_url: str
    published_at: datetime
    created_at: datetime

    class Config:
        from_attributes = True


class DevotionVerseResponse(BaseModel):
    """Devotion verse response"""

    id: int
    verse_text: str
    reference: str
    date: datetime
    created_at: datetime

    class Config:
        from_attributes = True


class DevotionNoteCreate(BaseModel):
    """Devotion note creation"""

    content: str
    date: Optional[datetime] = None


class DevotionNoteUpdate(BaseModel):
    """Devotion note update"""

    content: str


class DevotionNoteResponse(BaseModel):
    """Devotion note response"""

    id: int
    user_id: int
    date: datetime
    content: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# KTV Schemas
class KtvSongCreate(BaseModel):
    """KTV song creation"""

    title: str
    artist: str
    duration: int
    song_code: Optional[str] = None
    thumbnail_url: Optional[str] = None


class KtvSongResponse(BaseModel):
    """KTV song response"""

    id: int
    title: str
    artist: str
    duration: int
    song_code: Optional[str]
    thumbnail_url: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True


class KtvQueueCreate(BaseModel):
    """KTV queue request"""

    song_id: int
    requester_id: Optional[int] = None


class KtvQueueResponse(BaseModel):
    """KTV queue response"""

    id: int
    song_id: int
    requester_id: Optional[int]
    order: int
    is_played: bool
    created_at: datetime

    class Config:
        from_attributes = True
