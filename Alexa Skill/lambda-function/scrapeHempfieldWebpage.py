"""
This is a Python template for Alexa to get you building skills (conversations) quickly.
"""

from __future__ import print_function
import feedparser as fp
#import feedparser as fp


# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }

def build_response(session_attributes, speechlet_response):
    print(speechlet_response['outputSpeech']['text'])
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }

def buildRSSDate(date):
    # Converts the date given by Alexa into the date format for the published date
    months = ['January', 'Feburary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    return date[-2:] + ' ' + months[int(date[6:7])-1] + ' ' + date[0:4]

def readRSS(typeCalendar, date):
    if typeCalendar == "Calendar":
        d = fp.parse('https://www.hempfieldsd.org/site/RSS.aspx?DomainID=4&ModuleInstanceID=1&PageID=2')
        buildRSSDate(date)
        entries = d['entries']
        foundDate = False
        for x in range(len(entries)):
            entry = entries[x]
            if date in entry['published']:
                return entry['title']
                foundDate = True
            elif foundDate == True:
                break
        if foundDate == False:
            return date + " has no events scheduled."

    elif typeCalendar == "Sports":
        '''Will be added at a later date once school's calendar's are updated.
        On an ics file right now and lambdea does not work well with downloading ics files from the web.
        Array will be used once '''

    sportsCalendars = {
        'Baseball': 'hempfieldsd.org_sesj50idh538e3niqi77pmoirc@group.calendar.google.com',
        'Bowling': 'hempfieldsd.org_lo461hll6hml3c7b81fm0prg3s@group.calendar.google.com',
        'Boys Basketball': 'hempfieldsd.org_0mudi9jjp60ttg6obnaeoe8604@group.calendar.google.com',
        'Boys Lacrosse': 'hempfieldsd.org_pqv141eu1er5qfskeg443jip8o@group.calendar.google.com',
        'Boys Soccer': 'hempfieldsd.org_jc1sceuvdteh1h1o47nh34met0@group.calendar.google.com',
        'Boys Tennis': 'hempfieldsd.org_7hm0c58kmq8fl6bv4tehbip2e8@group.calendar.google.com',
        'Boys Volleyball': 'hempfieldsd.org_pk961db628spm2ak4q1i0qp0js@group.calendar.google.com',
        'Cross Country': 'hempfieldsd.org_apb1dvvnj55q37ohjngd7abu6o@group.calendar.google.com',
        'Field Hockey': 'hempfieldsd.org_4g6dk5gkft4apv9j31udo18tk4@group.calendar.google.com',
        'Football': 'hempfieldsd.org_da9mq0msp8i08obt45lupe6kvk@group.calendar.google.com',
        'Girls Basketball': 'hempfieldsd.org_dncumacujctkb9eo2rnpp95990@group.calendar.google.com',
        'Girls Lacrosse': 'hempfieldsd.org_e2o9r1kiq20vbioiurthinjt4o@group.calendar.google.com',
        'Girls Soccer': 'hempfieldsd.org_8qa20s47og5mnlob9llm43oosc@group.calendar.google.com',
        'Girls Tennis': 'hempfieldsd.org_eetrt8ds98ljl6uqit553ab4jk@group.calendar.google.com',
        'Girls Volleyball': 'hempfieldsd.org_h7r79q7ssnd9l401915hojs5no@group.calendar.google.com',
        'Golf': 'hempfieldsd.org_uulfpjqm4n6h8en813c8fo53ic@group.calendar.google.com',
        'Softball': 'hempfieldsd.org_h8122fmqpn2naqa8h4oe9ugk54@group.calendar.google.com',
        'Spring Track & Field': 'hempfieldsd.org_fe4c99mq2t2i1viimouk8ll56o@group.calendar.google.com',
        'Swimming and Diving': 'hempfieldsd.org_7ursu8u8b65e2av9g01t2nct9g@group.calendar.google.com',
        'Winter Track': 'hempfieldsd.org_mepschtcat6rlhkbqquouse0t0@group.calendar.google.com',
        'Wrestling': 'hempfieldsd.org_r1n1tn5dlidklei9hmrivmf2kg@group.calendar.google.com'
    }

def read_calendar(typeCalendar, date):
    if typeCalendar == "Sports":
        return "Sports Calendar support will be coming soon! Sorry!"
    elif typeCalendar == "Calendar":
        return readRSS
    else:
        return "No Calendar Selected"


def read_menu(menuType, date):
    if menuType == "lunch":
        return "Lunch Menu support will be coming soon! Sorry!"
    elif menuType == "breakfast":
        return "Breakfast Menu support will be coming soon! Sorry!"
    else:
        return "No Menu Selected"

def get_calendar_response():
    """ An example of a custom intent. Same structure as welcome message, just make sure to add this intent
    in your alexa skill in order for it to work.
    """
    session_attributes = {}
    card_title = "Calendar"
    speech_output = read_calendar("Calendar", "Today")
    reprompt_text = "You never responded to the first message. Sending another one."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def get_sports_schedule_response():
    """ An example of a custom intent. Same structure as welcome message, just make sure to add this intent
    in your alexa skill in order for it to work.
    """
    session_attributes = {}
    card_title = "Sports Schedule"
    speech_output = read_calendar("Sports", "Today")
    reprompt_text = "You never responded to the first message. Sending another one."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def get_menu_response(intentObj):
    """ An example of a custom intent. Same structure as welcome message, just make sure to add this intent
    in your alexa skill in order for it to work.
    """
    session_attributes = {}
    menuType = intentObj['slots']['menu']['value']
    date = intentObj['slots']['date']['value']
    card_title = menuType + "Menu"
    speech_output = read_menu(menuType, date)
    reprompt_text = "You never responded to the first message. Sending another one."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def get_welcome_response():
    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Welcome to the Hempfield Skill!"
    reprompt_text = "I don't know if you heard me, welcome to the Hempfield"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Keep working hard" \
                    "Have a nice day! "
    should_end_session = True
    return build_response({}, build_speechlet_response(card_title, speech_output, None, should_end_session))

def on_session_started(session_started_request, session):
    """ Called when the session starts.
        One possible use of this function is to initialize specific
        variables from a previous state stored in an external database
    """
    # Add additional code here as needed
    pass



def on_launch(launch_request, session):
    return get_welcome_response()


def on_intent(intent_request, session):

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']
    if intent_name == "ReadCalendar":
        return get_calendar_response()
    elif intent_name == "ReadSportsSchedule":
        return get_sports_schedule_response()
    elif intent_name == "ReadMenu":
        return get_menu_response(intent)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid command")


def on_session_ended(session_ended_request, session):
    print("on_session_ended requestId=" + session_ended_request['requestId'] + ", sessionId=" + session['sessionId'])

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("Incoming request...")

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    #if (event['session']['application']['applicationId'] != "amzn1.ask.skill.b02de4f0-b1f8-4819-82ab-855db97eaf6b"):
    #    raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']}, event['session'])
    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
