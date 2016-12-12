import os
from twilio.rest import TwilioRestClient

account_sid = os.environ["TWILIO_SID"]
#"{{ account_sid }}" # Your Account SID from www.twilio.com/console
auth_token  = os.environ["TWILIO_AUTH"]
#"{{ auth_token }}"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello from checkin",
    to="+13158065939",    # Replace with your phone number
    from_="+15005550006") # Replace with your Twilio number

print(message.sid)
