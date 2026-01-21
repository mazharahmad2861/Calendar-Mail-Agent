
from fastapi import FastAPI
from app.routers import auth, agent

app = FastAPI(title="Calendar Agent")

app.include_router(auth.router)
app.include_router(agent.router)
