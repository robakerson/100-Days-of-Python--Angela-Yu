import tkinter

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    with open("passwords.txt", "a") as file:
        file.write(f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n")
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
generate_button = tkinter.Button(text="Generate Password")
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
