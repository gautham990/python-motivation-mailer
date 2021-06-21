import datetime as dt
import random
import smtplib


def quotes_sender():
    random_quote = random.choice(all_quotes)
    my_email = "mymail@gmail.com"
    password = "mypass"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="pawemo4800@0ranges.com",
                            msg=f"Subject:Quote of the day\n\n{random_quote}")


with open("quotes.txt") as quotes_file:
    all_quotes = quotes_file.readlines()

today = dt.datetime.now().weekday()
if today == 0:
    quotes_sender()
