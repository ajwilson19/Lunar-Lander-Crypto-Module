import requests
import json
import matplotlib.pyplot as plt

symbol = input("Enter asset ticker: ")
data_points = "240" #input("Enter # of hours: ")
attributes = ["volatility"]

print("Pulling Data...")
link = "https://api.lunarcrush.com/v2?data=assets&key=dj4tgdk9258k4d9yl0ebm&symbol=" + symbol + "&data_points=" + data_points + "&interval=hours"
response = requests.get(url=link)
json_object = json.loads(response.text)

x = []
y = []
i = 0

data = json_object['data']
data_dict = data[0]
for hour in data_dict['timeSeries']:
    print()
    for elem in hour:
        # print(elem, hour[elem])
        if elem in attributes:
            x.append(i)
            i += 1
            y.append(hour[elem])  

plt.plot(x, y)
plt.xlabel("hours")
plt.ylabel(attributes[0])
plt.show()          