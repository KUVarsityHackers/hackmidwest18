from flask import Flask, request, Response
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from databaseHandler import *
import os.path
import datetime
import vobject
import requests
from dateutil import parser
from models import EventState, AttendeeState

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        return handle_request(request.form)

def handle_request(request_data):
    response = MessagingResponse()
    body = request_data['Body']
    phone_number = request_data['From']

    state = getState(phone_number)

    if type(state) is EventState:
        if state == EventState.EVENT_CREATED:
            nameEvent(phone_number, body)
            response.message('Your event has been called "{}". When would you like to have your event?'.format(body))
            return str(response)

        elif state == EventState.NAME_CREATED:
            setDatetimeEvent(phone_number, parser.parse(body))
            response.message('Your event has been schedule for {}. How would you describe your event?'.format(body))
            return str(response)

        elif state == EventState.TIME_CREATED:
            setDescriptionEvent(phone_number, body)
            response.message("Your event has the description: {}. How many people would you like to invite?".format(body))
            return str(response)
        
        elif state == EventState.DESCRIPTION_CREATED:
            setCapEvent(phone_number, body)
            response.message("You have invited {} people. Would you like this event to be Private, Friends of Friends, or Public?".format(body))
            return str(response)

        elif state == EventState.CAPCITY_CREATED:
            setVisibilityEvent(phone_number, parseVisibility(body))
            response.message("Visibility set. What's your name?")
            return str(response)

        elif state == EventState.VISIBILITY_CREATED:
            setCreatorNameEvent(phone_number, body)
            response.message("Hello {}, who would you like to event?".format(body))
            return str(response)
        # TODO: Logic for Adding attendees

    elif type(state) is AttendeeState:
        print("Fuck")

    else:
        if body == 'START':
            if createEvent(phone_number):
                response.message("What would you like to name your event?")
                return str(response)
            else:
                response.message("Please finish editing your other event first")
                return str(response)

def parseVisibility(body):
    if body.lower() == 'private':
        return 0
    elif body.lower() == 'friends of friends':
        return 1
    else:
        return 100
    
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
    if not os.path.isfile('database.db'):
        initializeDatabase()
    app.run(host='0.0.0.0', port=5000)
