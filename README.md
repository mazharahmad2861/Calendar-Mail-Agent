
# Calendar Mail Agent 
AI Calendar Agent  integrates directly with Gmail and Google Calendar using OAuth2. The agent understands natural-language questions like “Do I have any interviews?” or “What’s my afternoon schedule?” and uses LangGraph to route the query to the right tool—Calendar, Gmail, or a RAG-based email search. It behaves like a personal AI assistant, just like Google Assistant or Copilot, but fully customizable.

## What Problem This Solves 

People waste time manually checking emails and calendar events.

Meeting schedules are spread across Gmail and Google Calendar. Searching for "interviews", "client calls", "reminders" is tedious. AI assistants today are not private or customizable.

My solution:
A local, intelligent AI agent that can access your real Gmail + Calendar and answer all scheduling-related queries automatically.

 ## Core Features 

✔ Natural Language Understanding

✔ OAuth2 login with Google

✔ Reads real Calendar events

✔ Searches real Gmail emails

✔ Detects interviews, meetings, invites

✔ RAG-powered email memory using ChromaDB

✔ LangGraph agent state machine

✔ FastAPI backend

✔ Deterministic tool routing

✔ Secure token storage (JSON)

## Architecture Overview 

User → FastAPI → LangGraph Agent → Tools → Gmail/Calendar/RAG → Response

A detailed flow:

User sends query (e.g., “What’s my afternoon schedule?”)

FastAPI receives it

Query goes to LangGraph

LangGraph: uses LLM to interpret query → routes to correct tool:

      1.Gmail search

      2.Calendar event reader

      2.RAG semantic search

Tool fetches real data

Agent formats the final answer

FastAPI returns JSON response







