# Multi-Agent Design

FinMind-Arena assembles five core AI agents plus an orchestrator to simulate a collaborative investment committee.

## Agent Roster
| Agent | Focus | Responsibilities | Model Candidates |
|-------|-------|------------------|------------------|
| 🧮 **Fundamental Analyst** | Financial statements & company health | Evaluate revenue growth, EPS, leverage, and cash flow trends. Produce long-term outlook and valuation commentary. | `ProsusAI/finbert`, `BLOOM`, `Llama-3` |
| 📈 **Technical Analyst** | Price action & indicators | Track MA, RSI, MACD, and other signals to assess momentum and near-term direction. | `TimeGPT`, `Informer`, `Temporal Fusion Transformer` |
| 🗞️ **News Analyst** | Event and headline impact | Summarize breaking news, rate sentiment, and flag catalysts or risks. | `facebook/bart-large-cnn`, `ProsusAI/finbert` |
| 💬 **Social Analyst** | Community sentiment | Mine Reddit, Twitter (X), and StockTwits conversations for crowd sentiment and consensus. | `cardiffnlp/twitter-roberta-base-sentiment`, `roberta-base-sentiment` |
| 🧠 **Decision Orchestrator** | Debate facilitation & consensus | Conduct multi-round debates, reconcile conflicting views, and issue final recommendation. | `GPT-4o-mini`, `Llama-3-70B`, ReAct / debate frameworks |

## Debate Cycle
```
Round 1: Agents present perspectives with evidence and confidence scores.
Round 2: Orchestrator challenges assumptions; agents rebut or update stances.
Round 3: Votes are cast and aggregated into a Buy / Hold / Sell decision.
```

## Collaboration Frameworks
- **LangChain Multi-Agent**: Handles tool routing, memory, and message passing.
- **Microsoft AutoGen**: Provides debate workflows and role-based agent templates.
- **Custom Logic**: Apply domain-specific heuristics for weighting agent confidence.

## Implementation Notes
- **Model Availability**: TimeGPT is a commercial API from Nixtla. If you need open-source deployments, consider `darts` implementations of TFT/Informer or libraries like `Kats` for classical baselines.
- **Confidence Scoring**: Normalize confidence outputs (e.g., 0–1 scale) so the orchestrator can combine opinions deterministically.
- **Guardrails**: Define validation rules (e.g., minimum data freshness, variance checks) that must pass before an agent issues a recommendation.
