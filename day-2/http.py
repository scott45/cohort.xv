import requests
import json

# get weather forecast data for Nairobi city

key = "69e7171295188958144216fbaef8f988"
city_id = 184742
api_url = "http://api.openweathermap.org/data/2.5/forecast?id=%d&appid=%s" % (city_id, key)

response = requests.get(api_url)

# Check authorization
if response.status_code == 401:
    print("Please check your api key")

# 200 signifies Ok response.
elif response.status_code == 200:
    # response translated to json
    weather_data = json.loads(response.text)
    print(weather_data)

