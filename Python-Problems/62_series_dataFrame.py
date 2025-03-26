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
# col = data.condition
# print(col)


# Get data in row
# row = data[data.day =="Monday"]
# print(row)

# Get data of row having the highest value
# high_value_row = data[data['temp'] == data['temp'].max()]
# print(high_value_row)
# high_value_row = data[data.temp == data.temp.max()]
# print(high_value_row)

# # celcius to fernhight
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# monday_temp_f = monday_temp * 9 / 5 + 32
# print(monday_temp_f)



