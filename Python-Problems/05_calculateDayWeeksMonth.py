# age = int(input('Enter age in years! '))
# day = age * 365
# weeks  = age * 52
# month  = age * 12

# print(f'you are {day} days, {weeks} weeks, and {month} months old!')



# count remaining days to turn into 90
current_age = int(input("Enter your current age! "))
remaining_years = 90 - current_age
left_days = remaining_years * 365
left_weeks = remaining_years * 52
left_months = remaining_years * 12

print(f"You have left {left_days} days, {left_weeks} weeks, {left_months} months, and {remaining_years} years")