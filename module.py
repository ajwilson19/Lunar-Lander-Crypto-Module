import requests
import json

link = "https://api.lunarcrush.com/v2?data=assets&key=dj4tgdk9258k4d9yl0ebm&symbol=XRP&data_points=30&interval=hour"
response = requests.get(url=link)
json_object = json.loads(response.text)
print(json_object)

# for data in json_object['data']:
#     print(data['volatility'])