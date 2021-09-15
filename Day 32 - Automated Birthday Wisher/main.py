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

import datetime as dt

now = dt.datetime.now()
print(now.year)

day_of_birth = dt.datetime(year= 1987, month)