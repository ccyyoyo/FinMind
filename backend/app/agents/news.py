from .base import BaseAnalyst, AgentMeta
from ..schemas.analysis import AgentOpinion


class NewsAnalyst(BaseAnalyst):
    def __init__(self) -> None:
        self.meta = AgentMeta(name="News Analyst", key="news")

    def analyze(self, symbol: str, window_days: int) -> AgentOpinion:
        rationale = (
            "Placeholder: Summarized recent headlines; no strong catalysts detected."
        )
        return AgentOpinion(
            agent="news", stance="hold", confidence=0.45, rationale=rationale
        )

