# Whatsapp-Autoreply-Bot
An Autoreply API using flask API.

### Uses
* Twilio
* Flask
* ngrok

## Set Up
* Clone the repository

  ``` git clone https://github.com/kulkarni-rajas/whatsapp-autoreply-bot.git ```

* Change Directory

  ``` cd whatsapp-autoreply-bot ```

* Setup virtual environment

  ``` python3 -m venv env ```
  
  ``` source env/bin/activate ```

* Install Packages

  ``` python -m pip install -r requirments.txt ```

* Run Script

  ``` python3 app.py ```

* In another terminal 

  ``` ngrok http 5000 ```

- Copy the https link from ngrok and paste it in the Twilio Console

- For detailed explaination and tutorial : https://www.twilio.com/blog/build-a-whatsapp-chatbot-with-python-flask-and-twilio
