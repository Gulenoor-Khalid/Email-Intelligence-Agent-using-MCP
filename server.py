from mcp.server.fastmcp import FastMCP
from gmail_utils import authenticate_gmail

mcp = FastMCP("EmailAgent")

@mcp.tool()
def get_recent_emails():

    service = authenticate_gmail()

    results = service.users().messages().list(
        userId='me',
        maxResults=5
    ).execute()

    messages = results.get('messages', [])

    return messages

if __name__ == "__main__":
    mcp.run()