from .base import BaseAnalyst, AgentMeta
from ..schemas.analysis import AgentOpinion


class TechnicalAnalyst(BaseAnalyst):
    def __init__(self) -> None:
        self.meta = AgentMeta(name="Technical Analyst", key="technical")

    def analyze(self, symbol: str, window_days: int) -> AgentOpinion:
        rationale = (
            "Placeholder: Checked MA/RSI/MACD signals; momentum appears mixed."
        )
        return AgentOpinion(
            agent="technical", stance="hold", confidence=0.5, rationale=rationale
        )

