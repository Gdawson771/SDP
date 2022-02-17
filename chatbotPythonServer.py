import logging
import os
 
from flask import Flask
from flask_ask import Ask, request, session, question, statement
import RPi.GPIO as GPIO
 
app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger('flask_ask').setLevel(logging.DEBUG)
 


@ask.launch
def launch():
    speech_text = 'Welcome to the Raspberry Pi alexa automation.'
    return question(speech_text).reprompt(speech_text).simple_card(speech_text)

@ask.intent('DispenseSpice', mapping = {'whatSpice':'whatSpice', 'meaurement' :'meaurement','quantity':'quantity'})
def DispenseSpice_Intent(whatSpice,meaurement,quantity):
    return statement(whatSpice + "spices received")

@ask.intent('AMAZON.HelpIntent')
def help():
    speech_text = 'You can say hello to me!'
    return question(speech_text).reprompt(speech_text).simple_card('HelloWorld', speech_text)
 
 
@ask.session_ended
def session_ended():
    return "{}", 200
 
 
if __name__ == '__main__':
    if 'ASK_VERIFY_REQUESTS' in os.environ:
        verify = str(os.environ.get('ASK_VERIFY_REQUESTS', '')).lower()
        if verify == 'false':
            app.config['ASK_VERIFY_REQUESTS'] = False
    app.run(debug=True)