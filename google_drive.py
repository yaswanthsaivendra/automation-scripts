import requests
import json
from typing import Dict

FILE_NAME = "sample.pdf"
FILE_PATH = "E://"
GOOGLE_DRIVE_FOLDER_ID = "enter google drive folder id here"  # add this if file needs to uploaded in folder
URL = "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart"
SECRET = "enter your secret key here"

headers = {
    'Authorization': f'Bearer {SECRET}'
}

payload: Dict = {
    "name": FILE_NAME,
    "parents": [GOOGLE_DRIVE_FOLDER_ID]         # add this if file needs to uploaded in folder
}

final_payload: Dict = {
    "data": ('metadata', json.dumps(payload), 'application/json; charset=UTF-8'),
    "file": open(FILE_PATH + FILE_NAME, "rb")
}

response = requests.post(URL, headers=headers, files=final_payload)

print(response.status_code)
print(response.text)
