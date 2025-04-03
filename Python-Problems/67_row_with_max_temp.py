import pandas as pd

data = pd.read_csv("weather_data.csv")

max_temp_row = data[data.temp == data.temp.max()]
print(max_temp_row)