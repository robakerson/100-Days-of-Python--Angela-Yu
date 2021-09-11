import tkinter
from tkinter import messagebox
import random
import pyperclip
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
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = website_entry.get()
    password = password_entry.get()
    email = email_entry.get()

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showerror(message="One of the fields is empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n"
                                                              f"Website: {website}\n"
                                                              f"Email: {email}\n"
                                                              f"Password:{password}\n"
                                                              f"Is it ok to save?")
        if is_ok:
            with open("passwords.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, 'end')
                email_entry.delete(0, 'end')
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
generate_button = tkinter.Button(text="Generate Password", command=generate_password)
add_button = tkinter.Button(text="Add", command=save_password)
generate_button.grid(column=3, row=4, sticky="EW")
add_button.grid(column=2, row=5, columnspan=2, sticky="EW")

# Entry fields
website_entry = tkinter.Entry()
email_entry = tkinter.Entry()
email_entry.insert(0, "DefaultEmail@gmail.com")
password_entry = tkinter.Entry()
website_entry.focus()
website_entry.grid(column=2, row=2, columnspan=2, sticky="EW")
email_entry.grid(column=2, row=3, columnspan=2, sticky="EW")
password_entry.grid(column=2, row=4, sticky="EW")


window.mainloop()
