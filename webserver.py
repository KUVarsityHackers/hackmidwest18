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
            response.message('When would you like to have your event? (MM/DD/YY HH:MM a/pm)')
            return str(response)

        elif state == EventState.NAME_CREATED:
            setDatetimeEvent(phone_number, parser.parse(body))
            response.message('How would you describe your event? Remember to include the location')
            return str(response)

        elif state == EventState.TIME_CREATED:
            setDescriptionEvent(phone_number, body)
            response.message("How many people would you like to invite?")
            return str(response)

        elif state == EventState.DESCRIPTION_CREATED:
            setCapEvent(phone_number, int(body))
            response.message("Would you like this event to be: \n1)Private \n2)Friends of Friends \n3)Public")
            return str(response)

        elif state == EventState.CAPACITY_CREATED:
            setVisibilityEvent(phone_number, parseVisibility(body))
            response.message("What's your name?")
            return str(response)

        elif state == EventState.VISIBILITY_CREATED:
            setCreatorNameEvent(phone_number, body)
            response.message("Send us the phone number of or contact of someone you want to invite")
            return str(response)
        elif state == EventState.ORGANIZER_NAME_CREATED or state == EventState.ATTENDEES_ADDED:
            if state == EventState.ATTENDEES_ADDED:
                if body == "DONE":
                    event_name = getOpenEventName(phone_number)
                    setDone(phone_number)
                    response.message("Thank you for planning {} with EventsEverywhere. We hope your event goes well.".format(event_name))
                    return str(response)
            NumMedia = request_data['NumMedia']
            contacts_list = []
            body = only_numerics(body)
            for i in range(int(NumMedia)):
                contacts_list.append(handle_vcf_url(request_data['MediaUrl' + str(i)]))
            if(len(body) == 10):
                contacts_list.append("+1" + str(body))
            elif(len(body) == 11):
                contacts_list.append("+" + str(body))
            elif len(contact_list) == 0:
                response.message("Invalid number format")
                return str(response)
            for invitee in contacts_list:
                sendInvite(phone_number, invitee)
            sendInviteSMS(phone_number, contacts_list)
            response.message("Send us the name or contact of someone else you'd like to invite, or type DONE")
            return str(response)


    elif type(state) is AttendeeState:
        if state == AttendeeState.INVITE_SENT or state == AttendeeState.INVITE_MAYBE:
            if body.lower() == 'yes':
                inviteAccepted(phone_number)
                response.message("Thank you for accepting. What's your name?")
                return str(response)
            elif body.lower() == 'no':
                inviteDeclined(phone_number)
                response.message("Sorry that you can't make it. Thank you for using Events Everywhere")
                return str(response)
            elif body.lower() == 'maybe':
                inviteMaybe(phone_number)
                response.message("Please respond yes or no when you know if you'll be able to make it")
                return str(response)
            else:
                response.message("Sorry we were unable to understand what you said. Please send yes, no, or maybe")
                return str(response)
        elif state == AttendeeState.INVITE_ACCEPTED:
            setAttendeeName(phone_number, body)
            response.message("Thank you we'll keep you updated")
            return str(response)

    else:
        if body == 'START':
            if createEvent(phone_number):
                response.message("Welcome! Thank you for planning your event with Events Everywhere. Please provide a name for your event.")
                return str(response)
            else:
                response.message("Please finish editing your other event first")
                return str(response)
        if body == 'HELP':
            response.message("Help message")
            return str(response)
    return("Unable to understand your message. Please try again or send HELP for help")

def parseVisibility(body):
    if body.lower() == 'private':
        return 0
    elif body.lower() == 'friends of friends':
        return 1
    else:
        return 100
def sendInviteSMS(sender, inviteesNumber):
    senderName = getPersonName(sender)
    eventName = getOpenEventName(sender)
    message = "You have been invited by %s to %s. Can you come?\nReply Yes, No, Maybe" % (senderName, eventName)

    for invitee in inviteesNumber:
        sendSMS(invitee, message)
    

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
