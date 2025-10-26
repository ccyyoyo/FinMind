# Data & Knowledge Sources

FinMind-Arena synthesizes multiple external signals to create a holistic market perspective.

## Primary Data Providers
| Category | Sources | Notes |
|----------|---------|-------|
| Market & Fundamentals | Yahoo Finance API, Finnhub, Alpha Vantage | Real-time quotes, OHLCV, financial statements, technical indicators. |
| News | NewsAPI, Google News | Headlines, articles, and metadata for event tracking and summarization. |
| Social Sentiment | Reddit, Twitter (X), StockTwits APIs | Crowd sentiment, trending tickers, emerging narratives. |

## Data Pipeline Responsibilities
- **Standardization**: Normalize disparate payloads into unified schemas (time series or event streams).
- **Storage**: Persist structured data in PostgreSQL + TimescaleDB for efficient temporal queries.
- **Embedding Memory**: Store vectorized summaries and historical analysis in Chroma or Weaviate.
- **Access Control**: Manage API keys and rate limits within backend configuration.

## Compliance & Reliability Considerations
- **Licensing**: Confirm the terms of service for Reddit, Twitter (X), and news providers when storing or redistributing content.
- **Rate Limits**: Implement exponential backoff and caching to stay under free-tier quotas.
- **Data Quality**: Validate ticker symbols and filter duplicate events before persisting to avoid skewing agent signals.
- **Latency Budget**: Prioritize incremental updates (e.g., latest candle, recent headlines) to keep response times predictable.

## RAG Memory Strategy
1. Log each agent's analysis and debate outcomes.
2. Generate embeddings for prior insights to inform future decisions.
3. Use vector search to surface relevant historical context during new debates.
4. Tag stored memories with market regimes or volatility bands so retrieval favors comparable contexts.
