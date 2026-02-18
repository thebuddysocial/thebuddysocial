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

### Phase 4 - Cal.com
- Embedded Cal.com "Scoping Call 15-mins" widget in Schedule section

### Phase 5 - Our Why Image & Netlify Deploy
- Replaced Our Why image with team photo, object-position: 30% center
- Created netlify-deploy/index.html for Netlify deployment

### Phase 6 - Video Integration
- Added TBS Intro video (MP4, 55MB) to Section 3 (Presented By)
- Replaced stock image thumbnail with actual video player
- Click-to-play/pause with animated overlay + play button
- Video starts muted, unmutes on play
- Synced to netlify-deploy/index.html

## Deployment
Push to GitHub → Netlify reads `netlify-deploy/index.html` → Site deploys

## Backlog
- P1: Replace stock service images
- P2: Mobile responsiveness fine-tuning
