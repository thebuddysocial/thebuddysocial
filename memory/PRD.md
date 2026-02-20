# PRD - The Buddy Social Live Preview

## Original Problem Statement
Pull GitHub repo (https://github.com/thebuddysocial/thebuddysocial, branch: Version-02) and set up for live editing. Static website for Dublin community events.

## Architecture
- **Frontend**: React app (CRA + Craco) serving `buddysocial.html` via iframe
- **Static Site**: `buddysocial.html` in `/app/frontend/public/` (mirrored to `netlify-deploy/index.html`)
- **Deployment**: Netlify via GitHub (netlify-deploy/index.html)
- **3rd Party**: Cal.com scheduling (popup mode), GSAP animations, Font Awesome icons

## Key Files
- `/app/frontend/public/buddysocial.html` - Main website HTML
- `/app/netlify-deploy/index.html` - Netlify deployment version (keep in sync)

## What's Been Implemented

### Sessions 1-5: Setup, featured card, countdown timer, schedule title, founder overlays, glitch fix, carousel speed, calendar swap/revert, mobile About Us, schedule nav fix, Cal.com popup

### Session 6: Founder Card Redesign (2026-02-20)
**Desktop:**
- Always-visible frosted glass pill badge at bottom-left of each card (LinkedIn icon with pulse ring + founder name)
- On hover: badge fades to opacity:0, full overlay with name + "Connect" button appears
- Badge links directly to LinkedIn profile

**Mobile:**
- Desktop hover overlay hidden
- Bottom bar with name + LinkedIn icon + external link arrow
- Shimmer animation on bars to signal interactivity
- Entire bar tappable, links to LinkedIn profile

## Pending / Backlog
- P1: Replace stock service section images with real photos
- P2: Full mobile responsive audit across all sections
- P2: Update TBD event dates when confirmed
