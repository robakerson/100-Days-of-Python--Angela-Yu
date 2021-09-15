import pandas
import datetime as dt
from random import *
import smtplib

LETTERS = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
birthdays = pandas.read_csv("birthdays.csv")
birthday_list = birthdays.to_dict(orient="records")

today = dt.datetime.now()
letters_to_send = []
for cur_birthday in birthday_list:
    month = cur_birthday["month"]
    day = cur_birthday["day"]
    if month == today.month and day == today.day:
        name = cur_birthday["name"]
        email = cur_birthday['email']
        random_letter = choice(LETTERS)
        with open(f"letter_templates/{random_letter}") as file:
            letter_text = file.read().replace("[NAME]", name)
        sender = "Private Person <from@example.com>"
        receiver = f"{email}"
        message = f"""\
            Subject: Hi Mailtrap
            To: {receiver}
            From: {sender}

            This is a test e-mail message."""
        print(sender, receiver, message)
        with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
            server.login("")
            server.sendmail(sender, receiver, message)
        # letters_to_send.append(cur_birthday)
        # letters_to_send.append(letter_text)


# for _ in range(0, int(len(letters_to_send)/2) + 1, 2):
#     sender = "Private Person <from@example.com>"
#     receiver = f"{letters_to_send[_]['email']}"
#     message = f"""\
#     Subject: Hi Mailtrap
#     To: {receiver}
#     From: {sender}
#
#     This is a test e-mail message."""
#     print(sender,receiver,message)
#     with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
#         server.login("")
#         server.sendmail(sender, receiver, message)
# #

# for _ in range(2):
# sender = "Private Person <from@example.com>"
# receiver = "A Test User <to@example.com>"
#
# message = f"""\
# Subject: Hi Mailtrap
# To: {receiver}
# From: {sender}
#
# This is a test e-mail message."""
# for _ in range(2):
#     with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
#         server.login("")
#         server.sendmail(sender, receiver, message)