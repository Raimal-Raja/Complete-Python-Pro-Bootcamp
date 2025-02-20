def is_leapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        return True
    return False

def days_in_month(year, month):
    month_days = [31,28, 31, 30, 31, 30, 31, 30, 31, 30, 31, 30]
    if month > 12 or month <1:
        return 'invalid month'
    if is_leapYear(year) and month == 2:
        return 29
    return month_days[month -1]

year = int(input('Enter year: '))
month = int(input('enter Month: '))

days = days_in_month(year, month)
print(days) 