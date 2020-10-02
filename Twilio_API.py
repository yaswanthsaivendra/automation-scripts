from twilio.rest import Client

# store the auth tokens in env vars

client = Client()

from_no = 'whatsapp:+14155238886'
to_no = 'whatsapp:' + os.environ.get('PHONE_NUMBER')

client.messages.create(body="Message to be sent", from_=from_no, to=to_no)

driver.close()