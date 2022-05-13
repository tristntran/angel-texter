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
texter = angel_text.AngelText(twilio_account, twilio_token, twilio_number)
msg = "Testing Hi Brother - Tristan"
phone = "14082052148"
texter.send_message(msg,phone)
# # send a message in the morning
# schedule.every().day.at("1:11").do(send_message, GOOD_MORNING_QUOTES)
# schedule.every().day.at("11:11").do(send_message, GOOD_MORNING_QUOTES)
# schedule.every().day.at("2:22").do(send_message, GOOD_MORNING_QUOTES)
# schedule.every().day.at("3:33").do(send_message, GOOD_MORNING_QUOTES)
# schedule.every().day.at("4:44").do(send_message, GOOD_MORNING_QUOTES)
# schedule.every().day.at("5:55").do(send_message, GOOD_MORNING_QUOTES)
# schedule.every().day.at("1:23").do(send_message, GOOD_MORNING_QUOTES)
# schedule.every().day.at("12:12").do(send_message, GOOD_MORNING_QUOTES)
# schedule.every().day.at("12:34").do(send_message, GOOD_MORNING_QUOTES)

# while True:
#     # Checks whether a scheduled task
#     # is pending to run or not
#     schedule.run_pending()
#     time.sleep(2)
