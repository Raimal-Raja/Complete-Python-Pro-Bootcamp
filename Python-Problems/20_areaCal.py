height = int(input("Enter height in meter: "))
width = int(input("Enter weidth in meter: "))

print('Calculating...')
numberOfCan = height * width / 5
round(numberOfCan, 2)
print(f'You will need {numberOfCan} cans of paint.')
