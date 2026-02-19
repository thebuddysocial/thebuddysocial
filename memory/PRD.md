# PRD - The Buddy Social Live Preview

## Original Problem Statement
Pull GitHub repo (https://github.com/thebuddysocial/thebuddysocial, branch: Version-02) and set up for live editing. Static website for Dublin community events (students & graduates).

## Architecture
- **Frontend**: React app (CRA + Craco) serving `buddysocial.html` via iframe
- **Backend**: FastAPI (basic status API, mostly unused for static site)
- **Static Site**: `buddysocial.html` in `/app/frontend/public/` (mirrored to `netlify-deploy/index.html`)
- **Deployment**: Netlify via GitHub (netlify-deploy/index.html)
- **3rd Party**: Cal.com scheduling embed, GSAP animations, Font Awesome icons

## Key Files
- `/app/frontend/public/buddysocial.html` - Main website HTML (served via iframe)
- `/app/netlify-deploy/index.html` - Netlify deployment version (keep in sync)

## What's Been Implemented

### Session 1 - Repo Pull & Initial UI (2026-01-19)
- Cloned repo, services running
- Section 5: Single featured card ("Goal Setting for 2026: Vision Boarding")
- Schedule section: Added "UPCOMING EVENTS" title
- History: Creative hover overlays on founder images (Sunetra, Aditya, Shefali) with LinkedIn links

### Session 2 - Countdown + Fixes (2026-01-19)
1. **Countdown Timer**: Live countdown to Feb 28, 2026 2PM in Section 5 featured card — subtle, premium design with days/hrs/min/sec
2. **Schedule Title**: "UPCOMING EVENTS" now on ONE line (inline spans)
3. **Mobile About Us Fix**: Forced visibility of about-us-text + all reveal elements on mobile, hidden decorative "About"/"Us" text with `!important`

## Pending / Backlog
- P1: Replace stock service section images with real photos
- P2: Mobile fine-tuning across all sections
- P2: Update event dates when confirmed (LinkedIn Over Latte 2, Hire Me Maybe 2)
