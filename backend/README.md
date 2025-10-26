# FinMind-Arena Backend

FastAPI scaffold for the FinMind-Arena multi-agent analysis system.

## Endpoints
- `GET /health` – Service health.
- `POST /analyze` – Run a placeholder multi-agent analysis.

Example request:
```
POST /analyze
{
  "symbol": "AAPL",
  "window_days": 90
}
```

## Run locally
```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r backend/requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000 --app-dir backend
```

## Docker
```bash
cp .env.example .env
docker compose up --build
```

Navigate to http://localhost:8000/docs for interactive API docs.

## Next steps
- Implement real data connectors (Yahoo/Finnhub/NewsAPI/Reddit/Twitter).
- Add debate orchestration and agent-specific logic.
- Persist outputs to PostgreSQL and vector store.

