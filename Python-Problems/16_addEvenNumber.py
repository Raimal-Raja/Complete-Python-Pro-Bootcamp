total_number = 0
sumOfAllNumbers = 0
for num in range(1, 101):
    total_number += 1
    if num %2 ==0:
        sumOfAllNumbers += num
    else:
        sumOfAllNumbers = sumOfAllNumbers
print(total_number)
print(sumOfAllNumbers)


#Method -2
total = 0
for number in range(2, 101, 2):
    total += number
print(total)

total2 = 0
for number in range(1, 101):
    if number %2 ==0:
        total2 += number
print(total2)