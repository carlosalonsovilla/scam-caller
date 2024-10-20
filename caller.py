import os
import time
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

#Load environment variables

account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')
twilio_number = os.getenv('TWILIO_NUMBER')

client = Client(account_sid, auth_token)

# Initiate call to specified number

def make_call(to_number):
    call = client.calls.create(
        to=to_number,
        from_=twilio_number,
        url='https://spamcallmessage-6994.twil.io/twiml' #URL hosting Twilio Function
    )

    print(f"Call initiated with ID: {call.sid}")

scammer_number = '' #Enter the number you would like to call

# This will keep running until the program is stopped (Crtl + c)
try:
    while True:
        print(f"Calling: {scammer_number}...")
        make_call(scammer_number)
        time.sleep(15)

except KeyboardInterrupt:
    print("\nProcess interrupted ")

