from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Path to your client secret JSON file
CLIENT_SECRET_FILE = 'client_secret.json'

# Replace this with your Blogger blog ID
BLOG_ID = '376398700167798008'

# Post details
POST_TITLE = "Test Post"
POST_CONTENT = "<p>This is a test post made using the Blogger API and OAuth 2.0 with client_secret.json.</p>"

def main():
    # Scopes required for Blogger API
    SCOPES = ["https://www.googleapis.com/auth/blogger"]

    # Authenticate and obtain credentials
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
    credentials = flow.run_local_server(port=0)

    # Build the Blogger API client
    blogger_service = build('blogger', 'v3', credentials=credentials)

    # Create a test post
    post_body = {
        "kind": "blogger#post",
        "title": POST_TITLE,
        "content": POST_CONTENT,
    }

    try:
        # Insert the post into the blog
        post = blogger_service.posts().insert(blogId=BLOG_ID, body=post_body).execute()
        print(f"Post published! Post ID: {post['id']}")
        print(f"Post URL: {post['url']}")
    except HttpError as error:
        print(f"An error occurred: {error}")

if __name__ == "__main__":
    main()
