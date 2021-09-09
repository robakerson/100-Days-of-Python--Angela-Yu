import tkinter

window = tkinter.Tk()

window.title("WINDOWS 13")
window.minsize(width=600, height=600)

# label
my_label = tkinter.Label(text="I AM A LABEL", font=("Arial", 24, "bold"))
# my_label.pack(side="bottom")
my_label.grid(column=10, row=10)

my_label["text"] = "New Text"
my_label.config(text="OLD TEXT")


# button
def button_clicked():
    my_label["text"] = input.get()

button = tkinter.Button(text="Click me", command=button_clicked)
# button.pack()
# button.place(x=10, y=10)
button.grid(column=0, row=0)
new_button = tkinter.Button(text="New Button")
new_button.grid(column=15, row=0)


# entry
input = tkinter.Entry(width=20)
# input.pack()
input.grid(column=20, row=20)
print(input.get())





window.mainloop()
