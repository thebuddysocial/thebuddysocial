# PRD - The Buddy Social Live Preview

## Original Problem Statement
Preview the GitHub repo (thebuddysocial/thebuddysocial) netlify-deploy/index.html in live preview mode with iterative design improvements.

## Architecture
- **Frontend**: React app serving full-viewport iframe to static HTML
- **Static Site**: `buddysocial.html` in `frontend/public/`
- **Backend**: FastAPI (unchanged)
- **Database**: MongoDB (unchanged)
- **3rd Party**: Cal.com embed for scheduling (https://cal.com/the-buddy-social)

## What's Been Implemented

### Phase 1 (2026-02-18) - Initial Setup
- Cloned repo, deployed as live preview via iframe

### Phase 2 (2026-02-18) - Content & Design Updates
1. Section 2 Photos: Replaced 5 stock photos with user's event photos
2. Services Section: Redesigned into premium numbered cards (01, 02, 03)
3. "Our Why" Spacing: Reduced excessive padding/margins

### Phase 3 (2026-02-18) - Carousel Expansion
- Added 5 new event photos interleaved between 4 existing images (9 unique, 18 total with loop duplicates)
- Slowed carousel animation to 50s for longer track

### Phase 4 (2026-02-18) - Section Backgrounds & Cal.com
1. **Section Backgrounds**: Reverted to original alternating cream/cream-light pattern (user preferred it)
2. **Cal.com Integration**: Embedded Cal.com inline booking widget (dark theme) in Schedule section
   - Shows "Scoping Call 15-mins" event type
   - Google Meet integration
   - Interactive calendar with available dates and time slots
   - Styled with dark wrapper matching schedule section aesthetic

## Backlog
- P1: Replace stock service images with user's own photos
- P2: Dynamic content via backend
- P2: Mobile responsiveness fine-tuning
