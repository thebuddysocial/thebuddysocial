# PRD - The Buddy Social Live Preview

## Original Problem Statement
Preview the GitHub repo (thebuddysocial/thebuddysocial) netlify-deploy/index.html in live preview mode with iterative design improvements.

## Architecture
- **Frontend**: React app serving full-viewport iframe to static HTML
- **Static Site**: `buddysocial.html` in `frontend/public/` + mirrored to `netlify-deploy/index.html`
- **Deployment**: Netlify reads from `netlify-deploy/index.html` via GitHub
- **3rd Party**: Cal.com embed for scheduling

## What's Been Implemented

### Phase 1 - Initial Setup
- Cloned repo, deployed as live preview via iframe

### Phase 2 - Content & Design
1. Section 2: Replaced 5 stock photos with user's event photos
2. Services: Redesigned into premium numbered cards (01, 02, 03)
3. Our Why: Reduced spacing

### Phase 3 - Carousel
- Added 5 new event photos interleaved (9 unique, 18 total)

### Phase 4 - Cal.com & Section Revert
- Reverted section backgrounds to alternating cream/cream-light
- Embedded Cal.com "Scoping Call 15-mins" widget in Schedule section

### Phase 5 - Our Why Image & Netlify Deploy
1. Replaced Our Why stock image with team photo (3 individuals)
2. Added object-position: 30% center to frame all 3 people properly
3. Created /app/netlify-deploy/index.html mirroring buddysocial.html for Netlify deployment

## Deployment Flow
- Push to GitHub → Netlify reads `netlify-deploy/index.html` → Site deploys
- Use "Save to Github" feature in Emergent chat to push changes

## Backlog
- P0: User to attach video (mentioned upcoming)
- P1: Replace stock service images
- P2: Mobile fine-tuning
