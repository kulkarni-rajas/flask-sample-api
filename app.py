from flask import Flask, request
import requests
import subprocess
import sys
import time,datetime   
import pytz 
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False


    if 'quote' in incoming_msg:
        # return a quote
        r = requests.get('https://api.quotable.io/random')
        if r.status_code == 200:
            data = r.json()
            quote = f'{data["content"]} ({data["author"]})'
        else:
            quote = 'I could not retrieve a quote at this time, sorry.'
        msg.body(quote)
        responded = True


    if 'cat' in incoming_msg:
        # return a cat pic
        msg.media('https://cataas.com/cat')
        responded = True


    if 'help' in incoming_msg:
        # return help message
        msg.body('''Hello there! \nTo set a Reminder type \n*Reminder HH:MM <Text Message>* ''')
        responded = True

    if 'reminder' in incoming_msg:
        time_format = '%H:%M'
        target_time = incoming_msg[9:14]
        target_message = incoming_msg[15:]
        current_time = datetime.datetime.now(pytz.timezone('Asia/Calcutta'))
        current_time_str = datetime.datetime.strftime(current_time,time_format)
        time_left = (datetime.datetime.strptime(target_time,time_format) - datetime.datetime.strptime(current_time_str,time_format)).total_seconds()
        
        while(time_left != 0):
            time.sleep(1)
            current_time = datetime.datetime.now(pytz.timezone('Asia/Calcutta'))
            current_time_str = datetime.datetime.strftime(current_time,time_format)
            time_left = (datetime.datetime.strptime(target_time,time_format) - datetime.datetime.strptime(current_time_str,time_format)).total_seconds()

        msg.body(f'{target_message}  {time_left}')
        responded = True


    if not responded:
        # default message if no case matches
        msg.body('''Sorry, I did not get you, I'm still learning \nType *Help* to know my skills''')


    return str(resp)


if __name__ == '__main__':
    app.run()