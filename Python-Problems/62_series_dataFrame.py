import pandas as pd

data = pd.read_csv('weather_data.csv')
#
# # convert to the list
# temp_list = data['temp'].to_list()
# print(temp_list)
#
# # find the average using sum function
# average = sum(temp_list) / len(temp_list)
# print(average)
#
# # find mean
# mean = data['temp'].mean()
# print(mean)
#
# # find mode
# mode = data['temp'].mode()
# print(mode)

# find max
# max_temp = data['temp'].max()
# print(max_temp)

# data_condition = data['condition']
# print(data_condition)

# get data columns directly
col = data.condition
print(col)