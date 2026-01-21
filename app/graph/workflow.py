from langgraph.graph import StateGraph
from app.tools.calendar_tool import fetch_calendar_events
from app.tools.gmail_tool import search_interviews


# 1) Router function → returns next node name
def router(state):
    q = state["query"].lower()

    if "interview" in q:
        return "gmail"
    else:
        return "calendar"


# 2) Calendar node function
def calendar_node(state):
    events = fetch_calendar_events()
    return {"result": events}


# 3) Gmail node function
def gmail_node(state):
    emails = search_interviews()
    return {"result": emails}


# 4) Build graph
graph = StateGraph(dict)

# Register nodes by NAME + function
graph.add_node("router", router)
graph.add_node("calendar", calendar_node)
graph.add_node("gmail", gmail_node)

# Entry point
graph.set_entry_point("router")

# Correct conditional edges
graph.add_conditional_edges(
    source="router",          # router node name
    condition=router,         # router function (callable)
    path={                    # mapping: router return -> node name
        "calendar": "calendar",
        "gmail": "gmail"
    }
)

# Compile graph
graph = graph.compile()


# Public runner
def run_agent(query: str):
    return graph.invoke({"query": query})
