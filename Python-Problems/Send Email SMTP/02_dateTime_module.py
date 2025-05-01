import datetime as dt

now = dt.datetime.now()
year =  now.year
month = now.month
weekday = now.weekday()
print(year)
print(weekday)
print(now)

my_date_of_birth =  dt.datetime(year=2004,month=3,day=9)
print(my_date_of_birth)