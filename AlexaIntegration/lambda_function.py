from __future__ import print_function
import json
from twilio.rest import Client


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
	speech_output = "Hello World "
	reprompt_text = None
	should_end_session = True
	return build_response({}, build_speechlet_response(speech_output, should_end_session))


def handle_session_end_request():
	card_title = "Session Ended"
	speech_output = "Goodbye "
	should_end_session = True
	return build_response({}, build_speechlet_response(speech_output, should_end_session))


def player_name(intent, session):
    session_attributes = {}
    number = intent['slots']['number']['value']
    reprompt_text = None
    name = returnName(number)
    speech_output = 'Number {} is {}'.format(number, name)
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(speech_output, should_end_session))


# --------------- Specific Events ------------------

def on_intent(intent_request, session):
	print("on_intent requestId=" + intent_request['requestId'] + ", sessionId=" + session['sessionId'])
	intent = intent_request['intent']
	intent_name = intent_request['intent']['name']
	if intent_name == "TestText":
		return player_name(intent, session)
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

def returnName(number):
    if number == "0":
        return "Marcus Garrett"
    elif number == "1":
        return "Dedric Lawson"
    elif number == "2":
        return "Lagerald Vick"
    elif number == "3":
        return "Sam Cunliffe"
    elif number == "4":
        return "Devonte Graham"
    elif number == "5":
        return "Charlie Moore"
    elif number == "10":
        return "Sviatoslav Mykhailiuk"
    elif number == "12":
        return "Chris Teahan"
    elif number == "13":
        return "K.J. Lawson"
    elif number == "14":
        return "Malik Newman"
    elif number == "21":
        return "Clay Young"
    elif number == "22":
        return "Silvio De Sousa"
    elif number == "35":
        return "Udoka Azubuike"
    elif number == "44":
        return "Mitch Lightfoot"
    elif number == "55":
        return "James Sosinski"
