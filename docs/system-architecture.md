# System Architecture

FinMind-Arena follows a layered architecture that separates data ingestion, agent reasoning, debate orchestration, and delivery of investment intelligence.

## Layered Flow
1. **Data Ingestion**
   - Aggregates real-time market, fundamental, news, and social sentiment data.
   - Normalizes inputs into time series or event streams.
   - Persists data in PostgreSQL enhanced with TimescaleDB for temporal queries.
2. **Multi-Agent Reasoning**
   - Dedicated agents analyze the ingested data from specialized perspectives.
   - Each agent produces insights, rationales, and confidence scores.
3. **Debate & Consensus Engine**
   - Orchestrates multi-turn debate rounds (present, challenge, reconcile).
   - Harmonizes agent viewpoints into a consolidated recommendation.
4. **Output Delivery**
   - Generates comprehensive reports and dashboards for end users.
   - Supports PDF export and interactive web experiences.

### Component Responsibilities
- **Ingestion Workers**: Run on a schedule or on-demand trigger; handle retries, API rate limits, and schema validation before persisting data.
- **Processing Pipelines**: Compute derived indicators (e.g., moving averages, sentiment scores) and enrich raw payloads for downstream agents.
- **Agent Runtime**: Executes reasoning chains, tracks intermediate thoughts, and emits structured responses (stance, evidence, confidence).
- **Consensus Layer**: Applies weighting heuristics, resolves conflicts, and writes summaries plus decisions back into the knowledge store.
- **Presentation Layer**: Reads the latest recommendation package and renders charts, debate transcripts, and downloadable artifacts.

### Cross-Cutting Concerns
- **Secrets Management**: Store API keys and model credentials in a vault or encrypted environment variables.
- **Observability**: Capture logs, metrics, and traces for ingestion throughput, agent latency, and debate outcomes.
- **Scalability**: Decouple long-running ingestion or model calls via task queues (e.g., Celery, BullMQ) when concurrency grows.
- **Fallbacks**: Define safe defaults when a data source is unavailable so the orchestrator can still reach a defensible conclusion.

## Suggested Tech Stack
| Layer        | Recommended Technologies |
|--------------|--------------------------|
| Frontend     | Next.js, Tailwind CSS, Chart.js |
| Backend      | FastAPI or Node.js, LangChain, Hugging Face Transformers |
| Database     | PostgreSQL + TimescaleDB |
| RAG Store    | Chroma or Weaviate |
| Deployment   | Zeabur, Render, or AWS EC2 |
| Model Access | HuggingFace Hub, OpenRouter |

## Architecture Diagram
```
[ User ]
   │
   ▼
Frontend (Next.js UI) ──► Backend API (FastAPI / Node)
   │                          │
   │                          ├── Multi-Agent Orchestrator
   │                          ├── Data Ingestion Services
   │                          ├── RAG Memory Manager
   │                          └── Report Generator
   │
   ├── Visualizations & Reports
   ▼
Cloud Services & APIs
   ├── Financial Data Sources (Yahoo, Finnhub, Alpha Vantage)
   ├── News & Social APIs (NewsAPI, Reddit, Twitter, StockTwits)
   ├── Hosted Models (HuggingFace Hub, OpenRouter)
   └── Vector Stores (Chroma, Weaviate)
```
