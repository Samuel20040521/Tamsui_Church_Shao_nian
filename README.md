# Tamsui Church Shao-nian Management System Requirements

## Installation

```bash
# 1. Clone the repository
git clone <repository-url>
cd Tamsui_Church_Shao_nian

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Initialize database
python -c "from app.database import init_db; init_db()"

# 5. Run the application
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Development

### Project Structure

```
app/
├── main.py                 # FastAPI application entry
├── database.py            # Database configuration
├── routers/               # API endpoint definitions
│   ├── home.py           # Home page endpoints
│   ├── record.py         # Record/gathering endpoints
│   ├── devotion.py       # Devotion endpoints
│   ├── profile.py        # User profile endpoints
│   ├── attendance.py     # Attendance/check-in endpoints
│   └── ktv.py            # KTV/song request endpoints
├── models/               # SQLAlchemy ORM models
│   └── base.py          # All database models
├── schemas/              # Pydantic request/response schemas
│   └── base.py          # All schemas
├── templates/            # Jinja2 HTML templates
│   ├── base.html        # Base layout template
│   ├── home.html        # Home page template
│   ├── record.html      # Record page template
│   ├── devotion.html    # Devotion page template
│   ├── profile.html     # Profile page template
│   └── components/      # Reusable template components
├── static/
│   ├── css/             # CSS files
│   │   └── style.css   # Custom Tailwind styles
│   └── js/              # JavaScript files
│       └── main.js     # Main application script
├── services/            # Business logic services
└── utils/              # Utility functions

migrations/             # Database migration files (Alembic)
tests/                 # Unit and integration tests
requirements.txt       # Python dependencies
.env.example          # Environment variables template
.gitignore           # Git ignore rules
```

### Key Features Implementation

#### 1. Home Page (主頁)
- Display current gathering information
- RSVP buttons (attend/not attend)
- TODO items section
- Real-time UI updates with htmx

#### 2. Records (紀錄)
- List past gatherings (newest first)
- Gathering photos and details
- Infinite scroll pagination
- Comments and likes functionality

#### 3. Devotion (靈修)
- Automatic YouTube video fetching from JAM channel
- Daily verse display
- User note-taking functionality
- Auto-save with AJAX

#### 4. Profile (個人)
- Edit nickname and bio
- Avatar upload
- Multiple Google OAuth account binding
- Account management

#### 5. Attendance (點名)
- NFC card check-in
- Dynamic QR code scanning
- Attendance management (admin only)
- Statistics view

#### 6. KTV (點歌)
- Song search and browsing
- Queue management
- Anonymous/authenticated song requests
- Admin controls for playback

## Technology Stack

### Backend
- **FastAPI** - Modern Python web framework
- **SQLAlchemy** - ORM for database operations
- **Jinja2** - Template rendering
- **Alembic** - Database migrations
- **SQLite/PostgreSQL** - Data persistence

### Frontend
- **Tailwind CSS** - Utility-first CSS framework
- **HTMX** - Server-driven HTML interactions
- **Alpine.js** - Lightweight JavaScript framework (optional)
- **Heroicons/Lucide** - Icon library

### DevOps
- **Uvicorn** - ASGI server
- **Docker** - Containerization (optional)
- **Raspberry Pi** - Hardware deployment target

## Configuration

### Environment Variables (.env)

```
DATABASE_URL=sqlite:///./tamsui_church.db
# Or PostgreSQL:
# DATABASE_URL=postgresql://user:password@localhost/tamsui_church

SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

YOUTUBE_API_KEY=your-youtube-api-key
JAM_CHANNEL_ID=UCxxxxxxxxxxxxx

GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret

# Server configuration
HOST=0.0.0.0
PORT=8000
DEBUG=True
```

## API Documentation

Once the app is running, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Testing

```bash
# Run tests
pytest

# Run with coverage
pytest --cov=app tests/
```

## Deployment

### Raspberry Pi Setup

```bash
# 1. Install Python 3.10+
sudo apt update
sudo apt install python3.10 python3.10-venv

# 2. Create app directory
mkdir -p /opt/tamsui-church
cd /opt/tamsui-church

# 3. Set up systemd service
sudo nano /etc/systemd/system/tamsui-church.service
```

Example systemd service file:

```ini
[Unit]
Description=Tamsui Church Shao-nian System
After=network.target

[Service]
Type=notify
User=pi
WorkingDirectory=/opt/tamsui-church
Environment="PATH=/opt/tamsui-church/venv/bin"
ExecStart=/opt/tamsui-church/venv/bin/python -m uvicorn app.main:app --host 0.0.0.0 --port 8000
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

```bash
# 4. Enable and start service
sudo systemctl daemon-reload
sudo systemctl enable tamsui-church
sudo systemctl start tamsui-church

# Check status
sudo systemctl status tamsui-church
```

## Development Checklist

- [ ] Database schema finalized
- [ ] User authentication implemented
- [ ] Home page functionality
- [ ] Attendance tracking system
- [ ] Record management
- [ ] Devotion content integration
- [ ] Profile management
- [ ] KTV song system
- [ ] Frontend responsive design
- [ ] Testing suite
- [ ] Documentation
- [ ] Deployment scripts
- [ ] Backup/restore procedures

## Future Enhancements

1. **NFC Integration**: Raspberry Pi with ACR122U reader
2. **Mobile App**: React Native or Flutter version
3. **Analytics Dashboard**: Attendance trends and insights
4. **Email Notifications**: Event reminders and updates
5. **Video Archive**: Local YouTube video caching
6. **Multi-language Support**: English and other languages
7. **Advanced Permissions**: Role-based access control
8. **File Storage**: Cloud backup (AWS S3, etc.)

## Support and Contribution

For issues or feature requests, please submit through the project repository.

---

*Last updated: 2025-12-06*
*Version: 0.1.0*
