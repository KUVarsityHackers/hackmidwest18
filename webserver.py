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
from twilio.rest import Client
from auth_token import account_sid, auth_token

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
            setNameEvent(phone_number, body)
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
            setCapEvent(phone_number, int(body))
            response.message("You have invited {} people. Would you like this event to be Private, Friends of Friends, or Public?".format(body))
            return str(response)

        elif state == EventState.CAPACITY_CREATED:
            setVisibilityEvent(phone_number, parseVisibility(body))
            response.message("Visibility set. What's your name?")
            return str(response)

        elif state == EventState.VISIBILITY_CREATED:
            setCreatorNameEvent(phone_number, body)
            response.message("Hello {}, who would you like to invite?".format(body))
            return str(response)
        elif state == EventState.ORGANIZER_NAME_CREATED or state == EventState.ATTENDEES_ADDED:
            if state == EventState.ATTENDEES_ADDED:
                if body == "DONE":
                    event_name = getOpenEventName(phone_number)
                    setDone(phone_number)
                    response.message("Thank you for planning {} with EventsEverywhere. We hope your event goes well.".format(eventName))
                    return str(response)
            NumMedia = request_data['NumMedia']
            contacts_list = list()
            for i in range(int(NumMedia)):
                contacts_list.append(handle_vcf_url(request_data['MediaUrl' + str(i)])):
            if(len(body) == 10):
                contacts_list.append("+1" + str(body))
            elif(len(body) == 11):
                contacts_list.append("+" + str(body))
            elif len(contact_list) == 0:

            for invitee in contacts_list:
                sendInvite(phone_number, invitee)
            response.message("Send us the name or contact of someone else you'd like to invite, or type DONE")
            return str(response)


    elif type(state) is AttendeeState:
        return("Fuck")

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
def sendInviteSMS(sender, inviteNumber):
    senderName = getPersonName(sender)
    eventName =

    message = "You have been invited by %s to %s at %s. Can you come?\nReply Yes, No, Maybe" % (senderName, eventName, eventTime)

def sendSMS(number, message):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to=number,
        from_="+12028038368",
        body=message)

    print(message.sid)

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
