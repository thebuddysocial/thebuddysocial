# PRD - GitHub Repo Live Preview

## Original Problem Statement
Preview the current GitHub repo in live preview mode.

## Architecture
- **Backend**: FastAPI (Python) on port 8001
- **Frontend**: React (CRA + Tailwind) on port 3000
- **Database**: MongoDB (localhost:27017, DB: test_database)
- **Process Manager**: Supervisor

## What's Been Implemented (2026-02-18)
- Existing boilerplate codebase running as-is
- Backend: FastAPI with `/api/` health endpoint, `/api/status` CRUD endpoints
- Frontend: React app with Emergent branding, connected to backend API
- All services running and verified via testing agent (100% pass rate)

## Core Endpoints
- `GET /api/` - Health check (returns "Hello World")
- `POST /api/status` - Create status check
- `GET /api/status` - List status checks

## Status
Live preview running at: https://github-viewer-live.preview.emergentagent.com

## Backlog
- P0: None (boilerplate running)
- P1: User can extend with custom features
- P2: UI customization, additional API endpoints
