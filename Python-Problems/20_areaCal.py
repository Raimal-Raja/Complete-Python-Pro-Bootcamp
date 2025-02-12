# height = int(input("Enter height in meter: "))
# width = int(input("Enter weidth in meter: "))

# print('Calculating...')
# numberOfCan = height * width / 5
# round(numberOfCan, 2)
# print(f'You will need {numberOfCan} cans of paint.')


# same thing using functions
import math
def paint_calc(height, width, cover):
    area = height * width
    numberOfcan = math.ceil(area/cover)
    round(numberOfcan, 2)
    print(f'You will need to buy {numberOfcan} cans of paint.')

test_h = int(input("Enter height of Wall in meter: "))
test_w = int(input("Enter width of wall in meter: "))
coverage = 5
paint_calc(height = test_h, width = test_w, cover = coverage)