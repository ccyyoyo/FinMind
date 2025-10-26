from pydantic import BaseModel, Field
from typing import List, Literal, Optional


class AnalysisRequest(BaseModel):
    symbol: str = Field(..., description="Ticker symbol, e.g., AAPL")
    window_days: int = Field(90, ge=1, le=3650, description="Analysis window in days")
    locale: Optional[str] = Field(None, description="Locale hint, e.g., en, zh-Hant")


class AgentOpinion(BaseModel):
    agent: Literal[
        "fundamental",
        "technical",
        "news",
        "social",
    ]
    stance: Literal["buy", "hold", "sell"]
    confidence: float = Field(ge=0.0, le=1.0)
    rationale: str


class AnalysisResponse(BaseModel):
    symbol: str
    recommendation: Literal["buy", "hold", "sell"]
    confidence: float = Field(ge=0.0, le=1.0)
    agent_opinions: List[AgentOpinion]
    debate_summary: str

