from .base import BaseAnalyst, AgentMeta
from ..schemas.analysis import AgentOpinion


class SocialAnalyst(BaseAnalyst):
    def __init__(self) -> None:
        self.meta = AgentMeta(name="Social Analyst", key="social")

    def analyze(self, symbol: str, window_days: int) -> AgentOpinion:
        rationale = (
            "Placeholder: Crowd sentiment neutral; no consensus-driven signal."
        )
        return AgentOpinion(
            agent="social", stance="hold", confidence=0.5, rationale=rationale
        )

