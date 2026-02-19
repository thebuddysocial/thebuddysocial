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
- Copied all files to /app directory structure
- Frontend and backend services running
- Website loads correctly with hero section, nav, animations

### Previous Phases (from repo history)
1. Foundation setup (Phases 1-5)
2. Phase 6 (2026-02-19) - Major content overhaul: section typography, upcoming events cards, about us, history, footer updates

## Pending / Backlog
- P0: User to share LinkedIn URLs for 3 founders
- P1: Replace stock service section images
- P2: Mobile fine-tuning
- User requested: UI edits (awaiting specifics)
