# FinMind-Arena

Comprehensive documentation for the FinMind-Arena project lives in the `docs/` directory. Start with `docs/README.md` for a tour of the system overview, architecture, agent design, data sources, and deployment plans.

## Initial Scaffold
- Backend (FastAPI): `backend/app`, Dockerfile at `backend/Dockerfile`
- Compose services: `docker-compose.yml` (API + TimescaleDB)
- API endpoints: `GET /health`, `POST /analyze`

Quick start:
- Copy env: `cp .env.example .env`
- Build & run: `docker compose up --build`
- Docs: visit `http://localhost:8000/docs`

Traditional Chinese docs: `docs/zh-hant/README.md`.
