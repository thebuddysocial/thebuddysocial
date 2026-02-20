# PRD - The Buddy Social Live Preview

## Original Problem Statement
Pull GitHub repo (https://github.com/thebuddysocial/thebuddysocial, branch: Version-02) and set up for live editing. Static website for Dublin community events.

## Architecture
- **Frontend**: React app (CRA + Craco) serving `buddysocial.html` via iframe
- **Static Site**: `buddysocial.html` in `/app/frontend/public/` (mirrored to `netlify-deploy/index.html`)
- **Deployment**: Netlify via GitHub (netlify-deploy/index.html)
- **3rd Party**: Cal.com scheduling embed (dark theme), GSAP animations, Font Awesome icons

## Key Files
- `/app/frontend/public/buddysocial.html` - Main website HTML
- `/app/netlify-deploy/index.html` - Netlify deployment version (keep in sync)

## What's Been Implemented

### Session 1-3: Initial setup, featured card, countdown, schedule title, founder LinkedIn overlays, title glitch fix

### Session 4: Carousel speed, calendar swap (Google), mobile About Us overlay

### Session 5: Mobile About Us + Cal.com Revert (2026-02-20)
1. **Mobile About Us**: Added `<h1 class="our-why-mobile-title">About Us</h1>` as centered header above image. Hidden on desktop (`display:none`), shown on mobile (`display:block`). Desktop "About"/"Us" side text hidden on mobile.
2. **Cal.com Restored**: Reverted Google Calendar iframe back to Cal.com embed with dark theme, month_view layout, brandColor #4D6731

## Pending / Backlog
- P1: Replace stock service section images with real photos
- P2: Full mobile responsive audit across all sections
- P2: Update TBD event dates when confirmed
