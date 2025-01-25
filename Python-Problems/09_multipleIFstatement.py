height = int(input("Enter your height in cm: "))
dollar = 0
photo = ''
if height > 120:
    print("you can rider! ")
    age = int(input('enter your age: '))
    if age >= 12 and age <18:
        dollar = 7
        print("do you want photos?")
        photo = input('Enter Y for Yes, and N for No: ')
        if photo == 'y':
            dollar += 3
            print(f"total bill is ${dollar}")
        else:
            print(f"total bill is ${dollar}")
    elif age <12:
        dollar = 5
        print("do you want photos?")
        photo = input("Enter Y for Yes and N for No: ")
        if photo == 'y':
            dollar += 3
            print(f"total bill is ${dollar}")
        else:
            print(f"total bill is ${dollar}")
            
    else:
        dollar = 12
        print("do you want photos?")
        photo = input("Enter Y for Yes and N for No: ")
        if photo == 'y':
            dollar += 3
            print(f"total bill is $ {dollar}")
        else:
            print(f"total bill is ${dollar}")
else:
    print("you can't ride! ")