
import tkinter
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_list = []
    password_list += [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, "end")
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- FIND PASSWORD ------------------------------- #


def find_password():
    website = website_entry.get()
    try:
        with open("passwords.json", "r") as file:
            data = json.load(file)
            try:
                website_data = data[website]
                messagebox.showinfo(title="Here is your password!", message=f"Website: {website},\n"
                                                                            f"Email: {website_data['email']},\n"
                                                                            f"Password: {website_data['password']}")
            except KeyError:
                messagebox.showinfo(title="Bad Website", message="No details for the website exists.")
    except FileNotFoundError:
        messagebox.showerror(title="UH OH", message="No Data File Found")

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = website_entry.get()
    password = password_entry.get()
    email = email_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showerror(message="One of the fields is empty!")
    else:
        try:
            with open("passwords.json", "r") as file:
                data = json.load(file)  # read .json file and create dictionary
                data.update(new_data)  # add data to end of current .json file
            with open("passwords.json", "w") as file:
                json.dump(data, file, indent=4)  # write new data to .json file
        except FileNotFoundError:  # if passwords.json doesn't exist
            with open("passwords.json", "w") as file:
                json.dump(new_data, file, indent=4)
        except ValueError:  # if passwords.json is empty but exists already
            with open("passwords.json", "w") as file:
                json.dump(new_data, file, indent=4)
        finally:  # always delete entry boxes
            website_entry.delete(0, 'end')
            password_entry.delete(0, 'end')

# ---------------------------- UI SETUP ------------------------------- #

# window display/logo image
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
canvas = tkinter.Canvas(width=200, height=200)
padlock_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=padlock_img)
canvas.grid(column=2, row=1)

# Labels
website_label = tkinter.Label(text="Website:")
email_label = tkinter.Label(text="Email/Username:")
password_label = tkinter.Label(text="Password:")
website_label.grid(column=1, row=2, sticky="EW")
email_label.grid(column=1, row=3, sticky="EW")
password_label.grid(column=1, row=4, sticky="EW")

# Buttons
search_button = tkinter.Button(text="Search", command=find_password)
generate_button = tkinter.Button(text="Generate Password", command=generate_password)
add_button = tkinter.Button(text="Add", command=save_password)
search_button.grid(column=3,row=2, sticky="EW")
generate_button.grid(column=3, row=4, sticky="EW")
add_button.grid(column=2, row=5, columnspan=2, sticky="EW")

# Entry fields
website_entry = tkinter.Entry()
email_entry = tkinter.Entry()
email_entry.insert(0, "DefaultEmail@gmail.com")
password_entry = tkinter.Entry()
website_entry.focus()
website_entry.grid(column=2, row=2, sticky="EW")
email_entry.grid(column=2, row=3, columnspan=2, sticky="EW")
password_entry.grid(column=2, row=4, sticky="EW")


window.mainloop()

# height = float(input("Height: "))
# weight = int(input("Weight: "))
#
# if height > 3:
#     raise ValueError("Height should not be higher than 3 meters.")
#
# BMI = weight / height ** 2
# print(bmi)



# try:
#     file = open("a_file.txt")
#     dict = {"key": "value"}
#     print(dict["wrong_key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist!")
# else:
#     content = file.read()
#     print(content)
#
# file.close()

#  try/except/else/finally:
#  try: try this first
#  except: do this if there was an exception
#  else: do this if there were NO exceptions
#  finally: do this no matter what
