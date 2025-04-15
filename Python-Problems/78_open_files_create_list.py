with open('text_1.txt') as file_1:
    data = file_1.readlines()
with open('text_2.txt') as file_2:
    data_1 = file_2.readlines()

final_list = [int(elem) for elem in data if elem in data_1]

print(final_list)