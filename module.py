import requests
import json
import pandas as pd

symbol = input("Enter asset ticker: ")
data_points = str(1) #input("Enter # of hours: ")

link = "https://api.lunarcrush.com/v2?data=assets&key=dj4tgdk9258k4d9yl0ebm&symbol=" + symbol + "&data_points=" + data_points + "&interval=hour"
response = requests.get(url=link)
json_object = json.loads(response.text)

# for data in json_object['data']:
#     for hour in data['timeSeries']:
#         if(hour['galaxy_score'] > 79):
#             if (hour['volatility'] < 0.016):
#                 print("Buy ", hour['close'], hour['volatility'])
#             else:
#                 print("Sell ", hour['close'])    

data = json_object['data']
data_dict = data[0]
for elem in data_dict:
    print(elem, data_dict[elem])