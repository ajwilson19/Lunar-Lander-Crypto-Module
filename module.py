import requests
import json
import pandas as pd

symbol = input("Enter asset ticker: ")
indicators = "galaxy_score,volatility,close"

link = "https://api.lunarcrush.com/v2?data=assets&key=dj4tgdk9258k4d9yl0ebm&symbol=" + symbol + "&data_points=12&time_series_indicators=" + indicators + "&indicators=" + indicators
response = requests.get(url=link)
json_object = json.loads(response.text)

for data in json_object['data']:
    for hour in data['timeSeries']:
        print(hour['galaxy_score'], hour['volatility'], hour['close'])