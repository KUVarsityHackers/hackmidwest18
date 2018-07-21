from flask import Flask, request, Response
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from databaseHandler import *
import os.path
import datatime
import vobject
import requests
# Events table
#  table

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
        createEvent(phone_number)
        response = MessagingResponse()
        response.message("What would you like to name your event?")
        return str(resp)
    else if
def handle_vcf_url(url):
    r = requests.get(url)
    vcard = vobject.readOne(r.text)
    tel = only_numerics(vcard.tel)
    if(len(tel) == 10):
        return "+1" + str(tel)
    elif(len(tel) == 11):
        return "+" + str(tel)
    else:
        raise TypeError('Cannot parse telephone number')

def only_numerics(seq):
    seq_type= type(seq)
    return seq_type().join(filter(seq_type.isdigit, seq))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
    if not os.path.isfile('database.db'):
        initializeDatabase()
