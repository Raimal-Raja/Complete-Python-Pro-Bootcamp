import pandas as pd
data = pd.read_csv('weather_data.csv')

temp_list = data['temp'].to_list()
print(temp_list)

average = sum(temp_list)/len(temp_list)
print(average)

mean = data['temp'].mean()
print(mean)

mode = data['temp'].mode()
print(mode)