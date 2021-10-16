import requests
import json

symbol = input("Enter asset ticker: ")
link = "https://api.lunarcrush.com/v2?data=assets&key=dj4tgdk9258k4d9yl0ebm&symbol=" + symbol + "&data_points=24&time_series_indicators=galaxy_score,volatility,close&indicators=galaxy_score,volatility,close"
response = requests.get(url=link)
json_object = json.loads(response.text)


for data in json_object['data']:
    for hour in data['timeSeries']:
        print(hour)
        print()     