# from app import app
from twilio.rest import Client
import random


def generate_code():
    return str(random.randrange(100000, 999999))

def send_sms(to_number, body):
    account_sid = 'ACf47c31d9ae7326a853f37ecec24bfdef'
    auth_token = 'dc68342dfa63281de3ab78131a9fa200'
    twilio_number = '+16196482390'
    client = Client(account_sid, auth_token)
    client.messages.create(to_number, from_=twilio_number, body=body)

# @classmethod
class TwilioHelper:

    def send_confirmation_code(self, to_number):
        verification_code = generate_code()
        send_sms(to_number, verification_code)
        print("send_confirmation")
        return verification_code    