import win32com.client
from twilio.rest import Client

outlook = win32com.client.Dispatch("Outlook.Application")
outlook_ns = outlook.GetNamespace("MAPI")



myfolder = outlook_ns.Folders["Michael_Tinker1@baylor.edu"].Folders["Inbox"]

messages = myfolder.Items

messagecount = 0

for message in messages:
    #if message.UnRead:
    #if message.UnRead == True:
    print(message.sender)
    print(message.subject)
    messagecount += 1

    if message.UnRead:
        print(message.sender)
        print(message.subject)

        if "absence" in message.subject:
            print("Found message with absence")

            Msg = outlook.CreateItem(0)
            Msg.Importance = 1
            Msg.Subject = 'Got your ' + message.subject + ' email'
            Msg.HTMLBody = 'Hi' + str(message.sender) + ',\n Sorry you are not well'

            Msg.To = message.sender.GetExchangeUser().PrimarySmtpAddress
            Msg.ReadReceiptRequested = True

            Msg.Send()



accountSID = "AC2d3aa0f6d18dfe8d06730f99c0538265"
authToken = "d821ed08d06959b46bdba18b39f55b4c"
client = Client(accountSID,authToken)
TwilioNumber = "+16098045645"
mycellphone = "+13464209748"

textmessage = client.messages.create(to=mycellphone, from_=TwilioNumber, body="You have " + str(messagecount) + " messages in your inbox.")

print(textmessage.status)