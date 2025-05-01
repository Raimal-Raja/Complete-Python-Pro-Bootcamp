import smtplib

my_email = "your email"
password = "your email password"

with  smtplib.SMTP("smtp.gmail.com", port=5000) as connection:
    connection.starttls() #transport layer security
    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr=my_email, to_addrs="your  partner email", msg="Subject: hello Professor \n\n Welcome to the Dark World")
