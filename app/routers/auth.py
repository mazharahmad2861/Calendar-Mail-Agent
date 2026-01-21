
from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from google_auth_oauthlib.flow import Flow
from app.config import CLIENT_SECRETS_FILE, SCOPES, REDIRECT_URI
import json, os

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.get("/login")
def login():
    flow = Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE,
        scopes=SCOPES,
        redirect_uri=REDIRECT_URI
    )
    auth_url, _ = flow.authorization_url(prompt='consent')
    return RedirectResponse(auth_url)

@router.get("/callback")
def callback(code: str):
    flow = Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE,
        scopes=SCOPES,
        redirect_uri=REDIRECT_URI
    )
    flow.fetch_token(code=code)
    creds = flow.credentials

    os.makedirs("tokens", exist_ok=True)
    with open("tokens/token.json", "w") as f:
        f.write(creds.to_json())

    return {"status": "OAuth successful"}
