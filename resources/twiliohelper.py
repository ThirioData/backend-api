# from app import app
from twilio.rest import Client
from authy.api import AuthyApiClient
import random

api = AuthyApiClient('MH4y8ZkYq7HHcnx683vVRJ7qWeabIpan')


def generate_code():
    return str(random.randrange(100000, 999999))

def send_sms(to_number, body):
    account_sid = 'ACf47c31d9ae7326a853f37ecec24bfdef'
    auth_token = 'dc68342dfa63281de3ab78131a9fa200'
    # auth_api_key = 'MH4y8ZkYq7HHcnx683vVRJ7qWeabIpan'
    twilio_number = '+16196482390'
    client = Client(account_sid, auth_token)
    api.phones.verification_start(to_number, '+91', via='sms')
    phoneNo = "+91" + to_number
    message = client.messages.create(phoneNo, from_=twilio_number, body=body)


class TwilioHelper:

    # @classmethod
    def send_confirmation_code(self, to_number):
        verification_code = generate_code()
        send_sms(to_number, verification_code)
        # print("send_confirmation")
        return verification_code

    def verify(self, phone_number, token):
        verification = api.phones.verification_check(phone_number, "+91", token)
        if verification.ok():
            return "success"

        # Error in verification    
        return "failure"