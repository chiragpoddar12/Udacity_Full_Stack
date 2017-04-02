from twilio.rest import TwilioRestClient

account_sid = "AC686b31b248eddf936d3fc27cf8341a5b" # Your Account SID from www.twilio.com/console
auth_token  = "9f475070ef24bb0458404a0dae4a37b6"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello Sanket",
    to="+919930935439",    # Replace with your phone number
    from_="+19032251131") # Replace with your Twilio number

print(message.sid)
