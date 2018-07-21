from flask import Flask, request, Response
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from databaseHandler import *
import os.path

# Events table
#  table

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        handle_request(request.form)
        return Response('', 204)

def handle_request(request_data):
    for key, value in request_data.items():
        print(key, value)

if __name__ == '__main__':
    if not os.path.isfile('database.db'):
        initializeDatabase()
    app.run(host='0.0.0.0', port=5000)