from .base import BaseAnalyst, AgentMeta
from ..schemas.analysis import AgentOpinion


class FundamentalAnalyst(BaseAnalyst):
    def __init__(self) -> None:
        self.meta = AgentMeta(name="Fundamental Analyst", key="fundamental")

    def analyze(self, symbol: str, window_days: int) -> AgentOpinion:
        rationale = (
            "Placeholder: Evaluated revenue, EPS, leverage, and cash flow. "
            "Insufficient fundamentals to deviate from neutral baseline."
        )
        return AgentOpinion(
            agent="fundamental", stance="hold", confidence=0.55, rationale=rationale
        )

