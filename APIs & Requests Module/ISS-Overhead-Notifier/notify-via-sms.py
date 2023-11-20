import os
import time
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import requests
from datetime import datetime

LAT = 18.520430
LNG = 73.856743
account_sid = 'AC433b32a2aabc6b8f4d600eaf833632d7'
auth_token = '2ceb693e4cd10e8c114fd1addcab7f27'

def is_iss_overhead():
    # getting ISS position from the API
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    # converting ISS position to float
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # checking if the ISS is close to the user's current position
    if LAT - 5 <= iss_latitude <= LAT + 5 and LNG - 5 <= iss_longitude <= LNG + 5:
        return True

def is_night():
    parameters = {
        "lat": LAT,
        "lng": LNG,
        "formatted": 0,
    }

    # getting sunset and sunrise timings from the API
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()

    # extracting sunrise and sunset timings from the response
    data = response.json()
    sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
    sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
    
    current_time = datetime.now().hour
    
    if current_time >= sunset or current_time <= sunrise:
        return True
    
while True:
    time.sleep(60) 
    if is_iss_overhead() and is_night():
        # sending sms to the user
        proxy_client = TwilioHttpClient()
        proxy_client.session.proxies = {'https': os.environ['https_proxy']}
        client = Client(account_sid, auth_token, http_client=proxy_client)
        message = client.messages.create(
        from_='+12567767982',
        to='+919028233983',
        body='Its going to rain today. Remember to bring an umbrella ☔️')
        print(message.status)
