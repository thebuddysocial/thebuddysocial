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
- `/app/frontend/src/App.js` - React wrapper (iframe embed)
- `/app/frontend/src/App.css` - Minimal CSS for iframe wrapper

## What's Been Implemented

### 2026-01-19 - Repo Pull & Setup
- Cloned repo from GitHub (Version-02 branch)
- All services running

### 2026-01-19 - UI Updates (Session 2)
1. **Section 5 (Upcoming Events)**: Replaced 2-card grid with single featured card matching live site — "Goal Setting for 2026: Vision Boarding" with image-left/content-right layout, Get Tickets CTA
2. **Schedule Section (2nd last)**: Added "UPCOMING EVENTS" title in cream/green-light on dark green background
3. **History Section - Founder LinkedIn**: Creative hover overlays on 3 founder images:
   - Left: Sunetra → linkedin.com/in/sunetra-bhattacharya/
   - Middle: Aditya → linkedin.com/in/adityabhatnagar1994/
   - Right: Shefali → linkedin.com/in/shefalitailor/
   - Hover shows name + glassmorphism "Connect" button with LinkedIn icon

### Previous Phases (from repo history)
- Phase 6 (2026-02-19): Section typography, upcoming events cards, about us, history, footer updates

## Pending / Backlog
- P1: Replace stock service section images
- P2: Mobile fine-tuning
- P2: Update event dates when confirmed
