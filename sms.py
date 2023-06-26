from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'ACaab5ad3d900e97f6c21dca6954f07126'
auth_token = 'd730b2f04ffd3dccd0bc5d6c699c036d'
client = Client(account_sid, auth_token)

def sendSMS(sender,recipient,body):
    message = client.messages \
                    .create(
                        body=body,
                        from_=sender,
                        to=recipient
                    )

    print(message.sid)