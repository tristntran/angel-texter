from twilio.rest import Client

class AngelText:
    def __init__(self,sid,token,number):
        self.sid = sid
        self.token = token
        self.number = number
        self.client = Client(self.sid, self.token)
        
    def send_message(self, msg: str, cellphone: str):
        """
        sends a designate message to a phone number

        :param msg: message to send
        :param cellphone: string of cell number for recipient
        """
        self.client.messages.create(to=cellphone,
                            from_=self.number,
                            body=msg
                            )

