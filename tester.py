import os
import requests
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# Set up required scopes for Google API
SCOPES = ['https://www.googleapis.com/auth/blogger']


def authenticate():
    creds = None
    # Check if token.json exists for saved credentials
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
            # Save the credentials for future use
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

    return creds


def main():
    # Authenticate and get credentials
    creds = authenticate()

    # Now you can use `creds` to make API calls
    print("Authentication successful!")


if __name__ == '__main__':
    main()