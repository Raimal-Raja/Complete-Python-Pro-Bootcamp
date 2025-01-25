# leapYear = int(input("Enter year: "))
while True:
    leapYear = int(input("Enter year: "))
    if leapYear % 4 == 0:
        if leapYear % 100 == 0:
            if leapYear % 400 == 0:
                print('it is a leap year!')
            else:
                print("it is not leap year!")
        else:
            print("It is a leap year!")
    else:
        print("It is not a leap year! ")