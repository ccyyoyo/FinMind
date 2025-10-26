from __future__ import annotations
from dataclasses import dataclass
from typing import Literal
from ..schemas.analysis import AgentOpinion


Stance = Literal["buy", "hold", "sell"]


@dataclass
class AgentMeta:
    name: str
    key: str


class BaseAnalyst:
    meta: AgentMeta

    def analyze(self, symbol: str, window_days: int) -> AgentOpinion:  # pragma: no cover - stub
        raise NotImplementedError

