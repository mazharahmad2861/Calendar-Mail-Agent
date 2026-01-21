
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import json

def get_services():
    creds = Credentials.from_authorized_user_file(
        "tokens/token.json",
        [
            "https://www.googleapis.com/auth/calendar.readonly",
            "https://www.googleapis.com/auth/gmail.readonly"
        ]
    )
    calendar = build("calendar", "v3", credentials=creds)
    gmail = build("gmail", "v1", credentials=creds)
    return calendar, gmail
