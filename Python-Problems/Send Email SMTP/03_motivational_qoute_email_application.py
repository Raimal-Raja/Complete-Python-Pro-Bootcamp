import smtplib
from quote import quote
import datetime  as dt
import random

MY_EMAIL = "your email"
PASSWORDS = "your email password"

now = dt.datetime.now()
weekday = now.weekday()
# print(weekday)
if weekday == 5:
    with open('quotes.txt') as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com", port=80) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORDS)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="your partner email", msg=f"Subject:Monday Motivation\n\n{quote}")

