from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle
from datetime import datetime, timedelta


#scopes = ["https://www.googleapis.com/auth/calendar"]

#flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes=scopes)
#credentials = flow.run_console()
#pickle.dump(credentials, open("token.pkl", "wb"))

credentials = pickle.load(open("token.pkl", "rb"))

service = build("calendar", "v3", credentials=credentials)

cal_result = service.calendarList().list().execute()  # returns all calendars

calendar_id = cal_result['items'][0]['id']

eve_result = service.events().list(calendarId=calendar_id).execute()  # returns all events

start_time = datetime.now() + timedelta (minutes = 15)
end_time = datetime.now() + timedelta (minutes = 30)

event = {
  'summary': 'test event',
  'location': 'home',
  'description': 'exploring calendar api',
  'start': {
    'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
    'timeZone': 'Asia/Kolkata',
  },
  'end': {
    'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
    'timeZone': 'Asia/Kolkata',
  },
  'reminders': {
    'useDefault': False,
    'overrides': [
      {'method': 'popup', 'minutes': 10},
    ],
  },
}

service.events().insert(calendarId=calendar_id, body=event).execute()

print("Event created successfully!!")