# PRD - The Buddy Social Live Preview

## Original Problem Statement
Pull GitHub repo (https://github.com/thebuddysocial/thebuddysocial, branch: Version-02) and set up for live editing. Static website for Dublin community events.

## Architecture
- **Frontend**: React app (CRA + Craco) serving `buddysocial.html` via iframe
- **Static Site**: `buddysocial.html` in `/app/frontend/public/` (mirrored to `netlify-deploy/index.html`)
- **Deployment**: Netlify via GitHub (netlify-deploy/index.html)
- **3rd Party**: Google Calendar embed, GSAP animations, Font Awesome icons

## Key Files
- `/app/frontend/public/buddysocial.html` - Main website HTML
- `/app/netlify-deploy/index.html` - Netlify deployment version (keep in sync)

## What's Been Implemented

### Session 1 - Repo Pull & Initial UI
- Section 5: Single featured card with countdown timer
- Schedule section: "UPCOMING EVENTS" title (one line)
- History: Founder hover overlays with LinkedIn links (Sunetra, Aditya, Shefali)

### Session 2 - Countdown + Fixes
- Live countdown timer to Feb 28, 2026 2PM
- Mobile About Us visibility fix

### Session 3 - Title Glitch Fix
- Removed TextScramble from History/Services titles

### Session 4 - Carousel, Calendar, Mobile About Us
1. **Mobile About Us**: "About"/"Us" text now overlays the image (cream text with shadow + dark gradient overlay)
2. **Carousel**: Speed increased (50s → 30s desktop, 18s mobile), infinite seamless loop
3. **Google Calendar**: Replaced Cal.com with Google Calendar appointment scheduling iframe

## Pending / Backlog
- P1: Replace stock service section images with real photos
- P2: Full mobile responsive audit across all sections
- P2: Update TBD event dates when confirmed
