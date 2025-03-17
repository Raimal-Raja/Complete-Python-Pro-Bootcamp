import pandas as pd
data = pd.read_csv('Central_Park_Census.csv.csv')
print(len(data))
count_gray = len(data[data['Primary Fur Color'] == 'Gray'])
print(count_gray)
count_red = len(data[data['Primary Fur Color'] == 'Cinnamon'])
print(count_red)
count_black = len(data[data['Primary Fur Color'] == 'Black'])
print(count_black)
