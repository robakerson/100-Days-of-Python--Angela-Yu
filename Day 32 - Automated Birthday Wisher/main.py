import pandas
import datetime as dt
from random import *
import smtplib

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
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
        random_letter = choice(LETTERS)
        with open(f"letter_templates/{random_letter}") as file:
            letter_text = file.read().replace("[NAME]", name)
        letters_to_send.append(letter_text)

print(letters_to_send)