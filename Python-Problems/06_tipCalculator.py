total = float(input("Enter total bill! "))
tip = float(input("how many you would like to give! "))
splitIntoPeople = int(input("How many to split the bill?"))

tip = tip / 100
tip2 = tip + 1.0

total = round(total * tip2, 2)
splitBill = total / splitIntoPeople

# tip = round(total * tip, 2)

print(f"each person should pay {splitBill}")

