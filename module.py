import requests
import json
import pandas as pd

symbol = "XRP" #input("Enter asset ticker: ")
data_points = input("Enter # of hours: ")
attributes = ["galaxy_score", "volatility", "close", "tweets"]
interval = "hour"

link = "https://api.lunarcrush.com/v2?data=assets&key=dj4tgdk9258k4d9yl0ebm&symbol=" + symbol + "&data_points=" + data_points + "&interval=" + interval
response = requests.get(url=link)
json_object = json.loads(response.text)

data = json_object['data']
data_dict = data[0]
for hour in data_dict['timeSeries']:
    #print(hour)
    for elem in hour:
        if elem in attributes:
            print(elem, hour[elem])
    print()