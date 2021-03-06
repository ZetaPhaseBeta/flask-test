from flask import Flask, request, Response
from datetime import datetime
import urllib.request
import urllib.parse
import requests
import pprint
import json
from flask_cors import CORS

application = Flask(__name__)
CORS(application)

OPENWEATHER_API_KEY = "37df39e9cf3691f235d7ad2fed75b01b"
open_weather_url = "http://api.openweathermap.org/data/2.5/weather"

@application.route("/")
def hello():
    header = "<h1>Below is the current time</h1></br>"
    body = "<h3>" + str(datetime.now()) + "</h3>"
    return header + body


@application.route("/weather/<city>")
def weather(city):
    url_string = open_weather_url + "?q=" + city.replace(" ", "+") + "&appid=" + OPENWEATHER_API_KEY
    response = requests.get(url_string)
    data = response.json()
    final_temp = ((9.0 / 5.0) * (int(data['main']['temp']) - 273) + 32)
    json_obj = {}
    json_obj['temperature'] = str(final_temp)
    json_string = json.dumps(json_obj)
    return Response(response=json_string, status=200, mimetype="application/json")

@application.route("/vue", methods=['POST'])
def vue():
    content = request.get_json()
    print(content)
    print(type(content))
    return "success"

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=80, debug=True)
