from twilio import rest

## Twilio credentials obtained from
## https://www.twilio.com/user/account/voice/dashboard
account_sid = "<account_sid>" 
auth_token = "<auth_token>"
client = rest.TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="One more final Test SMS Send Functionality",
                               to="+14696488107",
                               from_="+14697897256")
print(message.sid)
