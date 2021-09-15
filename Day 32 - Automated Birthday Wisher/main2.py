# import datetime as dt
# import smtplib
# from random import *
# today = dt.datetime.now()
#
#
# with open("quotes.txt") as file:
#     quotes = file.readlines()
# quote = choice(quotes)
#
# sender = "Private Person <from@example.com>"
# receiver = "A Test User <to@example.com>"
#
# message = f"""\
# Subject: Today's quote
# To: {receiver}
# From: {sender}
#
# {quote}"""
#
# if today.weekday() == 1:
#     with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
#         server.login("private")
#         server.sendmail(sender, receiver, message)


# import smtplib
#
# sender = "John Flask <johnflask@gmail.com>"
# receiver = "A Test User <to@example.com>"
#
# message = f"""\
# Subject: Hi Mailtrap
# To: {receiver}
# From: {sender}
#
# WHAT """
#
# with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
#     server.login("lookitup")
#     server.sendmail(sender, receiver, message)


# import datetime as dt
#
# now = dt.datetime.now()
# print(now.year)
#
# day_of_birth = dt.datetime(year=1987, month=5, day=11, hour=1)
# print(day_of_birth)
