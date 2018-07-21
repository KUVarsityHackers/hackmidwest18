from flask import Flask, request, Response
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from databaseHandler import *
import os.path
import datatime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        handle_request(request.form)
        return Response('', 204)

def handle_request(request_data):
    body = request_data['Body']
    phone_number = request_data['From']

    if body == 'START':
        if createEvent(phone_number):
            response = MessagingResponse()
            response.message("What would you like to name your event?")
            return str(response)
        else:
            response = MessagingResponse()
            response.message("Please finish editing your other event first")
            return str(response)

    elif nameEvent(body, phone_number):
        response = MessagingResponse()
        response.message('Your event has been called "{}"'.format(body))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    if not os.path.isfile('database.db'):
        initializeDatabase()