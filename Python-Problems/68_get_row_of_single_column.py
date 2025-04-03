import pandas as pd

data = pd.read_csv("weather_data.csv")
monday = data[data.day == 'Monday']
temperature_in_Kalvin_of_monday = monday.temp+273
print(temperature_in_Kalvin_of_monday)