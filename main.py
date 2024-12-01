# google blog automation using the google blogger api
import os
import requests
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# Set up required scopes for Google API
SCOPES = ['https://www.googleapis.com/auth/blogger']


def authenticate():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds


def create_draft_post(creds, blog_id, title, content):
    # Prepare the JSON payload for creating a draft post
    payload = {
        "title": title,
        "content": content,
        "status": "draft"  # Set status to 'draft'
    }

    # Make the POST request to create a new draft post
    response = requests.post(
        f'https://blogger.googleapis.com/v3/blogs/{blog_id}/posts?key=YOUR_API_KEY',
        headers={
            'Authorization': f'Bearer {creds.token}',
            'Content-Type': 'application/json'
        },
        json=payload
    )

    if response.status_code == 200:
        print("Draft post created successfully!")
        print(response.json())
    else:
        print(f"Failed to create draft post: {response.status_code} - {response.text}")


def main():
    # Authenticate and get credentials
    creds = authenticate()

    # Define your blog ID and API key here
    blog_id = '376398700167798008'  # Replace with your actual Blog ID

    # Define the title and content for the draft post
    title = "My New Draft Post"
    content = "<p>This is the content of my new draft post.</p>"

    # Create a new draft post
    create_draft_post(creds, blog_id, title, content)


if __name__ == '__main__':
    main()
