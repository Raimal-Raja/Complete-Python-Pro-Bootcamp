# with open("weather_data.csv") as file:
#     content = file.readlines()
#     print(content)
#
# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas
import pandas as pd

data = pandas.read_csv("weather_data.csv")
# print(data['temp'])
data_dict = data.to_dict()
print(data_dict)

