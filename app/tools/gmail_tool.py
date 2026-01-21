
from app.services.google_client import get_services

def search_interviews():
    _, gmail = get_services()
    res = gmail.users().messages().list(
        userId="me",
        q="interview OR meeting"
    ).execute()
    return res.get("messages", [])
