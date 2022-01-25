import os
import requests
import logging
import configparser
from alerts import email_alert

def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['openweathermap']['api']
def get_users():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return [config['openweathermap']['user1'], config['openweathermap']['user2']]

email_to = get_users()

api_key = get_api_key()
endpoint = 'https://api.openweathermap.org/data/2.5/onecall'

weather_params = {
    "lat": 28.239740,
    "lon": -82.322270,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}


response = requests.get(endpoint, params=weather_params)
response.raise_for_status()


possible_rain = False
weather_data = response.json()
final_data = weather_data["hourly"][:24]
for data in final_data:
    weather_code = data["weather"][0]["id"]
    if int(weather_code) < 700:
        possible_rain = True

if possible_rain:
    logging.basicConfig(format='%(asctime)s %(message)s',filename='alerts.log',level=logging.INFO)
    logging.info('Rain alert sent.')
    email_alert(email_to,"RAIN ALERT", "Check the weather it's going to rain\nmessage sent from my pi rain alert script")

else:
    print("no umbrella needed")