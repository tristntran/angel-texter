import random, schedule, time

from twilio.rest import Client
import json
import os
import angel_text
print(os.getcwd())
with open("./src/twilio-security.json") as f:
    twilio_credentials = json.load(f)
    twilio_account= twilio_credentials["sid"]
    twilio_token = twilio_credentials["token"]
    twilio_number = twilio_credentials["phone_number"]
phone = "13036188166"
texter = angel_text.AngelText(twilio_account, twilio_token, twilio_number,phone)
msg = "Hi Arianna. This is your angel speaking."

# texter.send_message(msg,phone)
# # send a message in the morning
schedule.every().day.at("00:00").do(texter.set_message)

while True:
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(2)
