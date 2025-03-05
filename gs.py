import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


def authenticate():
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://mail.google.com/']
    REDIRECT_URI = ""
    creds = None

    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = Flow.from_client_secrets_file(
                "credentials.json",
                scopes=SCOPES,
                redirect_uri=REDIRECT_URI,
            )

            auth_url, _ = flow.authorization_url(prompt="consent")
            print(f"Please go to this URL and authorize the application: {auth_url}")

            # After the user authorizes, they will be redirected to `aaa.com`
            auth_code = input("Enter the authorization code from the URL: ")
            flow.fetch_token(code=auth_code)
            creds = flow.credentials

            with open("token.json", "w") as token:
                token.write(creds.to_json())

    return creds

def main():
    SAMPLE_SPREADSHEET_ID = ""
    SAMPLE_RANGE_NAME = ""
    creds = authenticate()
    ocData = {}
    list_of_people = []
    try:
        service = build("sheets", "v4", credentials=creds)
        sheet = service.spreadsheets()
        result = (
            sheet.values()
            .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
            .execute()
        )
        values = result.get("values", [])

        if not values:
          print("No data found.")
          return

        for row in values[1:]:
          ocData = {'ocDate':row[0], 'personName':row[1], 'personEmail':row[2]}
          list_of_people.append(ocData)        
        
    except HttpError as err:
        print(err)

    return list_of_people   

