import time
import smtplib
import requests
from datetime import datetime

MY_EMAIL = "michaelandjello1564@gmail.com"
MY_PASSWORD = "**********"

LAT = 18.520430
LNG = 73.856743

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
        # sending email to the user
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, 
            to_addrs="parthsolanke@gmail.com", 
            msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
        )
