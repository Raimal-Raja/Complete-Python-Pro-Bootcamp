import datetime as dt
import smtplib

import pandas  as pd
import random

MY_EMAIL = "your email"
PASSWORD = "your password"

today = (dt.datetime.now().month, dt.datetime.now().day)
data  = pd.read_csv('birthdays.csv')

birthday_dict = {(data_row.month, data_row.day ): data_row for (index,data_row) in data.iterrows()}
# print(birthday_dict)
# print(today)
if today in birthday_dict:
    birthday_person = birthday_dict[today]
    path = f"letter_tamplates/letter_{random.randint(1,3)}.txt"
    with open(path) as letter_file:
        content = letter_file.readline()
        content.replace("[NAME]", (birthday_person['name']))
        # print(birthday_person['name'])

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL,PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person.email,
            msg=f"Subject:Happy Birthday!\n\n{content}"
        )
