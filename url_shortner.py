# --- Imports --- #
import requests

# --------------- # 

BASE_URI = "https://da.gd/s?url="

# ask input from User.
URL = input("- Enter The Link, you want to shorten...\n---> ")
REQ_URI = BASE_URI + URL

# make a request to dagd
req = requests.get(REQ_URI).text

# print output
print("--- Url Shortened ---\n")
print(f"- Given Url : {URL}")
print(f"- Shortened Url : {req}")
