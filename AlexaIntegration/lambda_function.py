from __future__ import print_function
import json
import requests
from twilio.rest import Client

account_sid = "AC81d02543e6fda0c44a977753c167e811"
auth_token = "b3fdab5ec0024c7807e243237f8572a4"

# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(output, should_end_session):
	return {
		'outputSpeech': {
			'type': 'PlainText',
			'text': output
		},
		'shouldEndSession': should_end_session
	}


def build_response(session_attributes, speechlet_response):
	return {
		'version': '1.0',
		'sessionAttributes': session_attributes,
		'response': speechlet_response
	}


# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():
	#session_attributes = {}
	card_title = "Welcome"
	speech_output = "Welcome to Events Everywhere. Say 'start' to begin creating an event."
	reprompt_text = None
	should_end_session = False
	return build_response({}, build_speechlet_response(speech_output, should_end_session))


def handle_session_end_request():
	card_title = "Session Ended"
	speech_output = "Goodbye "
	should_end_session = True
	return build_response({}, build_speechlet_response(speech_output, should_end_session))


def test_text(intent, session):
    session_attributes = {}
    #number = intent['slots']['number']['value']
    reprompt_text = None
    #name = returnName(number)
    #send_text("test", session_attributes.phone_number)
    speech_output = 'Text has been sent'
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(speech_output, should_end_session))


def start_create(intent, session):
    session_attributes = {}
    speech_output = "To start, please tell me your phone number."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(speech_output, should_end_session))


def phone_number(intent, session):
    number = intent['slots']['phoneNumber']['value']
    session['attributes']
    session['attributes']['phone_number'] = number
    reprompt_text = "What is your phone number?"
    send_text("START", number)
    speech_output = get_response_speech(1)
    should_end_session = False
    return build_response(session['attributes'], build_speechlet_response(speech_output, should_end_session))


def  set_name(intent, session):
    session['attributes']['event_name'] = intent['slots']['eventName']['value']
    send_text(intent['slots']['eventName']['value'], session['attributes']['phone_number'])
    speech_output = get_response_speech(2)
    should_end_session = False
    return build_response(session['attributes'], build_speechlet_response(speech_output, should_end_session))


def  set_date(intent, session):
    send_text(intent['slots']['date']['value'] + intent['slots']['time']['value'], session['attributes']['phone_number'])
    send_text(session['attributes']['event_name'], session['attributes']['phone_number'])
    speech_output = get_response_speech(3)
    should_end_session = False
    return build_response(session['attributes'], build_speechlet_response(speech_output, should_end_session))

def  set_cap(intent, session):
    send_text(intent['slots']['eventCapacity']['value'], session['attributes']['phone_number'])
    speech_output = get_response_speech(4)
    should_end_session = False
    return build_response(session['attributes'], build_speechlet_response(speech_output, should_end_session))


def  set_my_name(intent, session):
    send_text(intent['slots']['myName']['value'], session['attributes']['phone_number'])
    speech_output = get_response_speech(5)
    should_end_session = False
    return build_response(session['attributes'], build_speechlet_response(speech_output, should_end_session))


def  invite(intent, session):
    if (intent['slots']['inviteePhoneNumber']['value']):
        send_text(intent['slots']['inviteePhoneNumber']['value'], session['attributes']['phone_number'])
        speech_output = get_response_speech(6)
    else:
        send_text("DONE", session['attributes']['phone_number'])
        speech_output = get_response_speech(7)
    should_end_session = False
    return build_response(session['attributes'], build_speechlet_response(speech_output, should_end_session))


# --------------- Specific Events ------------------

def on_intent(intent_request, session):
	print("on_intent requestId=" + intent_request['requestId'] + ", sessionId=" + session['sessionId'])
	intent = intent_request['intent']
	intent_name = intent_request['intent']['name']
	if intent_name == "TestText":
		return test_text(intent, session)
	elif intent_name == "StartCreate":
		return start_create(intent, session)
	elif intent_name == "SetPhoneNumber":
		return phone_number(intent, session)
	elif intent_name == "SetDate":
		return set_date(intent, session)
	elif intent_name == "SetCap":
		return set_cap(intent, session)
	elif intent_name == "SetMyName":
		return set_my_name(intent, session)
	elif intent_name == "Invite":
		return invite(intent, session)
	elif intent_name == "AMAZON.HelpIntent":
		return get_welcome_response()
	elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
		return handle_session_end_request()
	else:
		raise ValueError("Invalid intent")

# --------------- Generic Events ------------------

def on_session_started(session_started_request, session):
	print("on_session_started requestId=" + session_started_request['requestId']+ ", sessionId=" + session['sessionId'])

def on_launch(launch_request, session):
	print("on_launch requestId=" + launch_request['requestId'] + ", sessionId=" + session['sessionId'])
	return get_welcome_response()

def on_session_ended(session_ended_request, session):
	print("on_session_ended requestId=" + session_ended_request['requestId'] + ", sessionId=" + session['sessionId'])


# --------------- Main handler ------------------

def lambda_handler(event, context):
	print("event.session.application.applicationId=" + event['session']['application']['applicationId'])
	if event['session']['new']:
		on_session_started({'requestId': event['request']['requestId']}, event['session'])
	if event['request']['type'] == "LaunchRequest":
		return on_launch(event['request'], event['session'])
	elif event['request']['type'] == "IntentRequest":
		return on_intent(event['request'], event['session'])
	elif event['request']['type'] == "SessionEndedRequest":
		return on_session_ended(event['request'], event['session'])


# --------------- Data Handler ------------------

def send_text(text_body, phone_number):
    client = Client(account_sid, auth_token)
    '''message = client.messages.create(
                              body= text_body,
                              from_= phone_number,
                              to='+19133279103'
                          )
    
    print(message.sid)'''
    r = requests.post("http://18.218.109.81", data={'Body': text_body, 'From': phone_number, 'NumMedia': 0})

def get_response_speech(num):
    if (num == 1):
        return "Phone number received. What would you like to name your event?"
    if (num == 2):
        return "Event named. What date and time will the event be?"
    if (num == 3):
        return "Date set. How many people do you need?"
    if (num == 4):
        return "Event capacity set. What is your name?"
    if (num == 5):
        return "If you'd like to invite somebody, please say invite and then their phone number. Otherwise say done."
    if (num == 6):
        return "You can invite another person by again saying invite and then their phone number. Otherwise you can say done."
    if (num == 7):
        return "Thank you for creating an event with Events Everywhere. The people you invited have been notified. Goodbye."