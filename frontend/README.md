# FinMind-Arena Frontend (Placeholder)

Recommended stack: Next.js + Tailwind CSS + Chart.js

Suggested structure:
- `app/` or `pages/` – routes
- `components/` – charts, debate timeline, summary cards
- `lib/api.ts` – backend API client (`/analyze`)
- `styles/` – global styles

Quick bootstrap (when ready):
```bash
npx create-next-app@latest frontend --ts --eslint --src-dir --app --tailwind
```

Core views:
- Home: input ticker + window; link to results
- Report: show recommendation, confidence, agent opinions, charts

Backend base URL via `NEXT_PUBLIC_API_BASE` env.

