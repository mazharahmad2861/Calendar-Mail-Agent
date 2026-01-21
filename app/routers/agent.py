
from fastapi import APIRouter
from app.graph.workflow import run_agent

router = APIRouter(tags=["Agent"])

@router.get("/ask")
def ask(q: str):
    return run_agent(q)
