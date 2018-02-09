# from app import app
from twilio.rest import Client
import random

class TwilioHelper:
    def generate_code(self):
        return str(random.randrange(100000, 999999))
    
    def send_sms(self, to_number, body):
        account_sid = app.config['TWILIO_ACCOUNT_SID']
        auth_token = app.config['TWILIO_AUTH_TOKEN']
        twilio_number = app.config['TWILIO_NUMBER']
        client = Client(account_sid, auth_token)
        client.api.messages.create(to_number, from_=twilio_number, body=body)

    # @classmethod
    def send_confirmation_code(self, to_number):
        verification_code = self.generate_code()
        self.send_sms(to_number, verification_code)
        print(to_number)
        return verification_code    