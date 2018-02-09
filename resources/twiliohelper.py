# from app import app
from twilio.rest import Client
import random

class TwilioHelper:
    def generate_code():
        return str(random.randrange(100000, 999999))
    
    def send_sms(to_number, body):
        account_sid = app.config['TWILIO_ACCOUNT_SID']
        auth_token = app.config['TWILIO_AUTH_TOKEN']
        twilio_number = app.config['TWILIO_NUMBER']
        client = Client(account_sid, auth_token)
        client.api.messages.create(to_number, from_=twilio_number, body=body)