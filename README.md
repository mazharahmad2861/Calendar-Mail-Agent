
# Calendar Agent (Full Production – OAuth2 + LangGraph)

## Overview
AI-powered Calendar Agent that answers natural language questions using:
- Google Calendar
- Gmail
- LangGraph (agent workflow)
- RAG (ChromaDB for email memory)
- FastAPI backend

## Features
- OAuth2 login with Google
- Real Gmail + Calendar access
- LangGraph-based agent router
- RAG email search
- JSON token storage (local dev)

## OAuth Redirect URI
http://localhost:8000/auth/callback

## Run
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Endpoints
- /auth/login
- /auth/callback
- /ask?q=...
