import requests
from twilio.rest import Client

LAT = 18.520430
LNG = 73.856743
API_Key = "f00ece292bc59e0f3277c98512265da7"
API_URL = "https://api.openweathermap.org/data/2.5/onecall"
parameters = {
    "lat": LAT,
    "lon": LNG,
    "appid": API_Key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=API_URL, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

account_sid = 'AC433b32a2aabc6b8f4d600eaf833632d7'
auth_token = '2ceb693e4cd10e8c114fd1addcab7f27'    
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    from_='+12567767982',
    to='+919028233983',
    body='Its going to rain today. Remember to bring an umbrella ☔️')
    print(message.status)
