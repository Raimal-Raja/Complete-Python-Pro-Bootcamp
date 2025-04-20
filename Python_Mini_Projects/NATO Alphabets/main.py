import pandas as pd

file_data = pd.read_csv('nato_phonetic_alphabet.csv')

phonetic_dict = {row.letter: row.code for (index, row) in  file_data.iterrows()}

word  = input("Enter word").upper()
# l = [letter for letter in word]
#
# for letter in l:
#     print(phonetic_dict[letter])

output_list =  [phonetic_dict[letter] for letter in word]
print(output_list)