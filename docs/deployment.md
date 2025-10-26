# Deployment Blueprint

This blueprint outlines how to deploy FinMind-Arena across frontend, backend, model services, and data infrastructure.

## Environment Responsibilities
| Component | Ownership | Platforms |
|-----------|-----------|-----------|
| Frontend (Next.js UI) | Your codebase | Deploy to Vercel or Zeabur for CI/CD simplicity. |
| Backend API (FastAPI / Node) | Your codebase | Host on Render, Zeabur, or AWS EC2. |
| Multi-Agent Orchestrator | Your codebase | Runs within backend service; leverages LangChain or AutoGen. |
| External Models | Managed service | Invoke via HuggingFace Inference API or OpenRouter. |
| Financial & Social APIs | Managed service | Connect to Yahoo Finance, Finnhub, NewsAPI, Reddit, Twitter. |
| Vector Database | Hybrid | Use Chroma, Weaviate, or Supabase Vector (self-hosted or managed). |

## Suggested Deployment Flow
1. **Frontend**: Push Next.js app to GitHub and connect Vercel for automatic builds.
2. **Backend**: Containerize FastAPI/Node app (Dockerfile) and deploy to Render/Zeabur with environment variables for API keys.
3. **Model Access**: Configure HuggingFace tokens or OpenRouter credentials; call remote inference endpoints.
4. **Database**: Provision PostgreSQL + TimescaleDB and a vector store. Supabase can host both relational and vector data.
5. **Monitoring**: Track API rate usage, orchestrator latency, and report generation throughput.

## Environment Management
- **Secrets**: Use platform-specific secrets stores (Render Secret Files, Zeabur Environment Variables, AWS Parameter Store) instead of hardcoding credentials.
- **Networking**: Restrict outbound traffic to approved API domains and secure database connections with TLS.
- **Testing Gates**: Automate integration tests (agent debate, ingestion smoke test) in CI before promoting to production.
- **Cost Controls**: Set usage alerts for third-party APIs and inference providers to catch anomalous spend early.

## Deployment Architecture Snapshot
```
Browser (User)
   │
   ▼
Vercel / Zeabur (Next.js Frontend)
   │
   ▼
Render / Zeabur / AWS EC2 (Backend API)
   ├── Multi-Agent Orchestrator
   ├── Data Ingestion Workers
   ├── RAG Memory Manager
   └── Report Generator
   │
   ├──► HuggingFace Hub (Model Inference)
   ├──► Financial & News APIs
   └──► Supabase / Chroma (Data Stores)
```

## Roadmap for Production Hardening
- Add authentication and quota management for end users.
- Automate CI/CD with GitHub Actions for both frontend and backend.
- Implement logging, tracing, and alerting (e.g., OpenTelemetry, Sentry).
- Evaluate container orchestration (Kubernetes) once traffic scales.
- Introduce feature flags for experimental agents or strategies to minimize production risk.
