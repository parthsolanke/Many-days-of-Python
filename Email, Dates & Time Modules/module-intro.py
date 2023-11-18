import smtplib
import datetime as dt

# Sending Email with Python

my_email = "dummy.senders.email@gmail.com"
password = "abcd1234()"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="dummy.recievers.email@gmail.com",
        msg="Subject:Hello\n\nThis is the body of my email."
    )


# Working with date and time in Python

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year=2000, month=12, day=15, hour=4)
print(date_of_birth)