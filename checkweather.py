
import json
from urllib.request import urlopen

apikey = "5dce37fb24b54d4086745a489df569f6"

def get_weather(city):
    sock = urlopen(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&units=metric")
    result = sock.read()
    sock.close()
    weather = json.loads(result)
    temperature = weather["main"]["temp"]
    feels_like = weather["main"]["feels_like"]
    humidity = weather["main"]["humidity"]

    return temperature, feels_like, humidity

invalid = False
user_city = input("Which city's weather would you like to check? ")
try:
    temperature_found, feels_like_temp, humidity = get_weather(user_city)
except:
    invalid = True # Catch exceptions so the program can gracefully terminate
if invalid:
    print("Invalid city, please try again.")
else:
    print(f"Weather in {user_city} is {temperature_found:.2f}°C with a feels like temperature of {feels_like_temp:.2f}°C with a humidity percentage of {humidity:.2f}%")
    print(f"Weather in {user_city} is {temperature_found:.2f}°C with a feels like temperature of {feels_like_temp:.2f}°C with a humidity percentage of {humidity:.2f}%")
