import tkinter

window = tkinter.Tk()

window.title("WINDOWS 13")
window.minsize(width=600, height=600)

# label
my_label = tkinter.Label(text="I AM A LABEL", font=("Arial", 24, "bold"))
my_label.pack(side="bottom")

my_label["text"] = "New Text"
my_label.config(text="OLD TEXT")


# button
def button_clicked():
    my_label["text"] = "YOU CLICKED THE BUTTON"


button = tkinter.Button(text="Click me", command=button_clicked)
button.pack()








window.mainloop()
