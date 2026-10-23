# UI Skeleton Implementation

This is the **Phase 1: UI Skeleton** implementation for the Tamsui Church Shao-nian Management System.

## What's Implemented

✅ **Mobile-First UI** with 4 bottom tabs (Spotify-style)
✅ **Home Page** - Current gathering info with attend/not attend buttons + TODO list
✅ **Record Page** - Past gatherings list with placeholder images
✅ **Devotion Page** - YouTube placeholder, daily verse, and notes area
✅ **Profile Page** - User avatar, nicknames, and Google accounts list
✅ **Responsive Layout** using Tailwind CSS
✅ **Clean Navigation** with active tab highlighting

## Quick Start

### 1. Install Dependencies

```bash
pip install fastapi uvicorn[standard] jinja2
```

### 2. Run the App

```bash
# Option 1: Using uvicorn directly
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Option 2: Using the test script
python test_app.py

# Option 3: Using Python module
python -m uvicorn app.main:app --reload
```

### 3. Open in Browser

- **Home**: http://localhost:8000/
- **Record**: http://localhost:8000/record
- **Devotion**: http://localhost:8000/devotion
- **Profile**: http://localhost:8000/profile

## File Structure

```
app/
├── main.py                  # FastAPI app with routes
├── routers/
│   ├── home.py             # Home page (/) with dummy data
│   ├── record.py           # Record page with past gatherings
│   ├── devotion.py         # Devotion page with verse & notes
│   └── profile.py          # Profile page with user info
├── templates/
│   ├── base.html           # Base template with bottom nav
│   ├── home.html           # Home page content
│   ├── record.html         # Record page content
│   ├── devotion.html       # Devotion page content
│   └── profile.html        # Profile page content
└── static/
    ├── css/style.css       # Custom styles
    └── js/main.js          # JavaScript utilities
```

## Features

### Home Page (/)
- **Current Gathering Block** (top 1/3):
  - Title, date, location
  - Main speaker, moderator, pianist
  - ✓ Attend / ✗ Not Attend buttons
- **TODO List** (bottom 2/3):
  - Checkboxes for tasks
  - Shows completion status

### Record Page (/record)
- **Past Gathering Cards**:
  - Sorted newest to oldest
  - Title and date
  - Placeholder gradient images
  - Clean card design

### Devotion Page (/devotion)
- **YouTube Placeholder** (16:9 aspect ratio):
  - Mock JAM channel video
  - Visual placeholder with icon
- **Daily Verse**:
  - Beautiful gradient background
  - Scripture text and reference
- **Notes Area**:
  - Large textarea for personal notes
  - Save button (visual only for now)

### Profile Page (/profile)
- **User Avatar**:
  - Circular gradient placeholder
  - User icon
- **Nicknames List**:
  - Multiple nicknames display
  - Add nickname button
- **Google Accounts**:
  - List of bound accounts
  - Add/Remove buttons (visual only)

## Design Principles

1. **Mobile-First**: Optimized for phone screens
2. **Clean & Simple**: Minimalist design with good spacing
3. **Tailwind CSS**: Utility-first styling
4. **No Database**: All dummy data for now
5. **No Authentication**: Login system comes later
6. **Static Pages**: Server-side rendering with Jinja2

## What's NOT Implemented Yet

❌ Database connections
❌ User authentication
❌ NFC check-in
❌ QR code generation
❌ YouTube API integration
❌ Google OAuth
❌ Real data persistence
❌ Form submissions
❌ Button functionality (except navigation)

These features will be implemented in future phases.

## Next Steps

**Phase 2** will add:
- Database models and connections
- User authentication system
- Real data CRUD operations
- Form handling and validation

**Phase 3** will add:
- External API integrations (YouTube, Google OAuth)
- NFC/QR code check-in
- File uploads (avatars, images)
- Advanced features

## Troubleshooting

### Port Already in Use
```bash
# Find and kill process using port 8000
lsof -ti:8000 | xargs kill -9
```

### Module Not Found
```bash
# Make sure you're in the project root
cd /Users/dengensheng/Developer/Tamsui_Church_Shao_nian

# Install dependencies
pip install -r requirements.txt
```

### Templates Not Found
```bash
# Verify directory structure
ls -la app/templates/
# Should show: base.html, home.html, record.html, devotion.html, profile.html
```

## Testing Checklist

- [ ] Home page loads at http://localhost:8000/
- [ ] All 4 bottom nav tabs are visible
- [ ] Clicking tabs navigates to correct pages
- [ ] Active tab is highlighted in blue
- [ ] Home page shows gathering info and TODO list
- [ ] Record page shows multiple past gatherings
- [ ] Devotion page shows video placeholder and verse
- [ ] Profile page shows avatar and account lists
- [ ] Layout is mobile-friendly (responsive)
- [ ] No console errors in browser dev tools

---

**Version**: 0.1.0 (UI Skeleton)  
**Last Updated**: 2025-12-06  
**Status**: ✅ Ready for Testing
