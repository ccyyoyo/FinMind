from typing import List
from ..schemas.analysis import AnalysisRequest, AnalysisResponse, AgentOpinion
from .debate import summarize_debate
from ..agents.fundamental import FundamentalAnalyst
from ..agents.technical import TechnicalAnalyst
from ..agents.news import NewsAnalyst
from ..agents.social import SocialAnalyst


class Orchestrator:
    """Coordinates agent analyses and produces a consolidated recommendation.

    This is a minimal scaffold that returns deterministic placeholders.
    Replace the internal logic with debate rounds and weighting heuristics.
    """

    def __init__(self) -> None:
        self.fundamental = FundamentalAnalyst()
        self.technical = TechnicalAnalyst()
        self.news = NewsAnalyst()
        self.social = SocialAnalyst()

    def analyze(self, req: AnalysisRequest) -> AnalysisResponse:
        opinions: List[AgentOpinion] = [
            self.fundamental.analyze(req.symbol, req.window_days),
            self.technical.analyze(req.symbol, req.window_days),
            self.news.analyze(req.symbol, req.window_days),
            self.social.analyze(req.symbol, req.window_days),
        ]

        # Simple consensus heuristic (placeholder):
        # map stance to numeric, average by confidence, then pick nearest.
        score_map = {"sell": -1.0, "hold": 0.0, "buy": 1.0}
        weighted = 0.0
        total_weight = 0.0
        for op in opinions:
            weighted += score_map[op.stance] * op.confidence
            total_weight += op.confidence

        avg = weighted / total_weight if total_weight else 0.0
        if avg > 0.25:
            rec = "buy"
        elif avg < -0.25:
            rec = "sell"
        else:
            rec = "hold"

        overall_conf = min(1.0, sum(op.confidence for op in opinions) / len(opinions))

        return AnalysisResponse(
            symbol=req.symbol.upper(),
            recommendation=rec,
            confidence=round(overall_conf, 2),
            agent_opinions=opinions,
            debate_summary=summarize_debate(opinions),
        )
