from fastapi import APIRouter, HTTPException
from ...schemas.analysis import AnalysisRequest, AnalysisResponse
from ...services.orchestrator import Orchestrator


router = APIRouter(prefix="/analyze", tags=["analysis"])


@router.post("", response_model=AnalysisResponse, summary="Run multi-agent stock analysis")
def analyze(request: AnalysisRequest):
    try:
        orchestrator = Orchestrator()
        result = orchestrator.analyze(request)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

