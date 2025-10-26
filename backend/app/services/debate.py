from ..schemas.analysis import AgentOpinion


def summarize_debate(opinions: list[AgentOpinion]) -> str:
    """Produce a simple textual summary from agent opinions.

    Replace with a real debate orchestration and summarization pipeline.
    """
    pieces = [f"{op.agent}: {op.stance} ({op.confidence:.2f})" for op in opinions]
    return "; ".join(pieces)

