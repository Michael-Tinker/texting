from twilio.rest import Client

accountSID = "AC2d3aa0f6d18dfe8d06730f99c0538265"
authToken = "d821ed08d06959b46bdba18b39f55b4c"
client = Client(accountSID,authToken)
TwilioNumber = "+16098045645"
mycellphone = "+13464209748"

textmessage = client.messages.create(to=mycellphone, from_=TwilioNumber, body="Hot singles in Egg Harbor New Jersey want to meet!")

print(textmessage.status)

#make a phone call
call = client.calls.create(url="http://demo.twilio.com/docs/voice.xml", to=mycellphone, from_=TwilioNumber)
