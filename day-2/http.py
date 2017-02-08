import requests
import json

# Let us get weather forecast data for Nairobi

key = "69e7171295188958144216fbaef8f988"
city_id = 184742
api_url = "http://api.openweathermap.org/data/2.5/forecast?id=%d&appid=%s" % (city_id, key)

response = requests.get(api_url)

# Check if you are authorized
if response.status_code == 401:
    print("Please check your api key")

# 200 means everything went well..so we can proceed to processing our response.
elif response.status_code == 200:
    # convert response to json
    weather_data = json.loads(response.text)
    print(weather_data)

# do something with the data
