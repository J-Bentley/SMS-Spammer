from twilio.rest import Client

#Enter account details (see: https://www.twilio.com/console)
account_sid = "AC...a1"
auth_token = "0a...6d"
twilioNumber = "+<countryCode><areaCode><senderTwilioNumber>" #ex +17054239654

client = Client(account_sid, auth_token)

receiver = input("Victim number including country/area code\n>>")
msg = input("Message (Free accounts append Twilio ad)\n>>")
msg_count = input("How many times?\n>>")

for x in range(0, int(msg_count)):

  client.api.account.messages.create(
    to = receiver,
    from_ = twilioNumber,
    body = msg)
	
print (msg, " sent to ",receiver,", ",str(msg_count)," times.")
