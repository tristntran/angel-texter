import random
from twilio.rest import Client
import json
from os import listdir
from os.path import isfile, join

class AngelText:
    def __init__(self,sid,token,number,cellphone):
        self.sid = sid
        self.token = token
        self.number = number
        self.cellphone = cellphone
        self.client = Client(self.sid, self.token)
        self.angel_times = {'1:11': [],
                            '2:22': [],
                            '3:33': [],
                            '4:44': [],
                            '5:55': [],
                            '10:10': [],
                            '11:11': [],
                            '12:12': [],
                            '12:34': [],
                            '13:11': [],
                            '14:22': [],
                            '15:33': [],
                            '16:44': [],
                            '17:55': [],
                            '22:10': [],
                            '23:11': []
                           }
    
    def init_angel_times(self,source_path):
        onlyfiles = [f for f in listdir(source_path) if isfile(join(source_path, f))]
        for file in onlyfiles:
            key = self.get_key(file)
            self.read_messages(key,file)

    def get_key(filename)-> str:
        key_start = filename.split('.')
        return key_start[:-2] + ':' + key_start[-2:]
 
    def read_messages(self,key,filepath):
        with open(filepath) as f:
            self.angel_times[key] = json.load(f)

    def send_message(self, msg: str):
        """
        sends a designate message to a phone number

        :param msg: message to send
        :param cellphone: string of cell number for recipient
        """
        self.client.messages.create(to=self.cellphone,
                            from_=self.number,
                            body=msg
                            )

    def send_angel_message(self,time):
        msg = random.choice(self.angel_times[time])
        if msg:
            self.send_message(msg)


    def set_message(self):
        times = ['1:11','2:22','3:33','4:44','5:55','10:10',
                 '11:11','12:12','12:34','13:11','14:22',
                 '15:33','16:44','17:55','22:10','23:11'
                ]
        if not random.randint(0,7):
            time = random.choice(times)
            self.send_angel_message(time)
