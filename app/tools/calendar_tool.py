
from app.services.google_client import get_services

def fetch_calendar_events():
    calendar, _ = get_services()
    events = calendar.events().list(
        calendarId="primary",
        maxResults=10,
        singleEvents=True,
        orderBy="startTime"
    ).execute()
    return events.get("items", [])
