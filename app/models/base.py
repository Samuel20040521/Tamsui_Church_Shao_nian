"""
SQLAlchemy models for database schema
"""

from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
    Boolean,
    ForeignKey,
    Float,
    Enum as SQLEnum,
)
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime
import enum


class User(Base):
    """User model"""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String, nullable=True)
    password_hash = Column(String, nullable=True)
    is_admin = Column(Boolean, default=False)
    is_leader = Column(Boolean, default=False)
    is_member = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    profile = relationship("UserProfile", back_populates="user", uselist=False)
    google_bindings = relationship("UserGoogleBinding", back_populates="user")
    attendance_records = relationship("Attendance", back_populates="user")
    devotion_notes = relationship("DevotionNote", back_populates="user")
    ktv_songs = relationship("KtvQueue", back_populates="requester")


class UserProfile(Base):
    """User profile model"""

    __tablename__ = "user_profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    nickname = Column(String, nullable=True)
    avatar_url = Column(String, nullable=True)
    bio = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    user = relationship("User", back_populates="profile")


class UserGoogleBinding(Base):
    """Google OAuth binding model"""

    __tablename__ = "user_google_bindings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    google_id = Column(String, unique=True, index=True)
    email = Column(String)
    name = Column(String)
    picture_url = Column(String, nullable=True)
    refresh_token = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    user = relationship("User", back_populates="google_bindings")


class Gathering(Base):
    """Gathering (聚會) model"""

    __tablename__ = "gatherings"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    date = Column(DateTime, index=True)
    location = Column(String, nullable=True)
    main_speaker = Column(String, nullable=True)
    moderator = Column(String, nullable=True)
    pianist = Column(String, nullable=True)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    attendance_records = relationship("Attendance", back_populates="gathering")
    record_post = relationship("RecordPost", back_populates="gathering", uselist=False)


class AttendanceStatus(str, enum.Enum):
    """Attendance status enum"""

    ATTEND = "attend"
    NOT_ATTEND = "not_attend"
    PENDING = "pending"


class Attendance(Base):
    """Attendance record model"""

    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)
    gathering_id = Column(Integer, ForeignKey("gatherings.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    status = Column(SQLEnum(AttendanceStatus), default=AttendanceStatus.PENDING)
    check_in_time = Column(DateTime, nullable=True)
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    gathering = relationship("Gathering", back_populates="attendance_records")
    user = relationship("User", back_populates="attendance_records")


class RecordPost(Base):
    """Weekly gathering record post"""

    __tablename__ = "record_posts"

    id = Column(Integer, primary_key=True, index=True)
    gathering_id = Column(Integer, ForeignKey("gatherings.id"), unique=True)
    title = Column(String)
    content = Column(Text, nullable=True)
    image_url = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    gathering = relationship("Gathering", back_populates="record_post")
    comments = relationship("RecordComment", back_populates="post")
    likes = relationship("RecordLike", back_populates="post")


class RecordComment(Base):
    """Comments on record posts"""

    __tablename__ = "record_comments"

    id = Column(Integer, primary_key=True, index=True)
    post_id = Column(Integer, ForeignKey("record_posts.id"))
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    content = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    post = relationship("RecordPost", back_populates="comments")


class RecordLike(Base):
    """Likes on record posts"""

    __tablename__ = "record_likes"

    id = Column(Integer, primary_key=True, index=True)
    post_id = Column(Integer, ForeignKey("record_posts.id"))
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    post = relationship("RecordPost", back_populates="likes")


class DevotionVideo(Base):
    """YouTube devotion video"""

    __tablename__ = "devotion_videos"

    id = Column(Integer, primary_key=True, index=True)
    youtube_id = Column(String, unique=True, index=True)
    title = Column(String)
    description = Column(Text, nullable=True)
    thumbnail_url = Column(String, nullable=True)
    video_url = Column(String)
    published_at = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)


class DevotionVerse(Base):
    """Daily devotion verse"""

    __tablename__ = "devotion_verses"

    id = Column(Integer, primary_key=True, index=True)
    verse_text = Column(Text)
    reference = Column(String)
    date = Column(DateTime, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class DevotionNote(Base):
    """User's personal devotion notes"""

    __tablename__ = "devotion_notes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    date = Column(DateTime, index=True)
    content = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    user = relationship("User", back_populates="devotion_notes")


class KtvSong(Base):
    """KTV song information"""

    __tablename__ = "ktv_songs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    artist = Column(String)
    duration = Column(Integer)  # in seconds
    song_code = Column(String, unique=True, nullable=True)
    thumbnail_url = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)


class KtvQueue(Base):
    """KTV play queue"""

    __tablename__ = "ktv_queues"

    id = Column(Integer, primary_key=True, index=True)
    song_id = Column(Integer, ForeignKey("ktv_songs.id"))
    requester_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    order = Column(Integer, index=True)
    is_played = Column(Boolean, default=False)
    played_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    requester = relationship("User", back_populates="ktv_songs")
