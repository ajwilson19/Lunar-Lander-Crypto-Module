import requests
import json
import pandas as pd

symbol = input("Enter asset ticker: ")
data_points = "1" #input("Enter # of hours: ")

link = "https://api.lunarcrush.com/v2?data=assets&key=dj4tgdk9258k4d9yl0ebm&symbol=" + symbol + "&data_points=" + data_points + "&interval=hour"
response = requests.get(url=link)
json_object = json.loads(response.text)

data = json_object['data']
data_dict = data[0]
for elem in data_dict:
    if elem in ["galaxy_score", "volatility", "close", "tweets"]:
        print(elem, data_dict[elem])