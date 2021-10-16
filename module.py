import requests
import json

link = "https://api.lunarcrush.com/v2?data=assets&key=dj4tgdk9258k4d9yl0ebm&symbol=XRP,QNT&data_points=4&time_series_indicators=galaxy_score,volatility,close&indicators=galaxy_score,volatility,close"
response = requests.get(url=link)
json_object = json.loads(response.text)
# print(json_object)

for data in json_object['data']:
    print(data['timeSeries'])
    print()