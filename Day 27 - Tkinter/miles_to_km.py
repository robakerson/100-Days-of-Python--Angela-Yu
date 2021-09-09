import tkinter
FONT = ("Arial", 24)

def calculate_km():
    result = float(num_entry.get()) * 1.609
    km_num["text"] = "{0:.2f}".format(result)

window = tkinter.Tk()
# window.minsize(width=350, height=200)
window.title("Convert miles to Km")
window.config(padx=20, pady=20)

miles_label = tkinter.Label(text="Miles", font=FONT)
miles_label.grid(column=3, row=1)

km_label = tkinter.Label(text="Km", font=FONT)
km_label.grid(column=3, row=2)

equals_label = tkinter.Label(text="is equal to", font=FONT)
equals_label.grid(column=1, row=2)

km_num = tkinter.Label(text="0", font=FONT)
km_num.grid(column=2, row=2)

calc_button = tkinter.Button(text="Calculate", command=calculate_km, width=15)
calc_button.grid(column=2, row=3)

num_entry = tkinter.Entry()
num_entry.grid(column=2, row=1)


window.mainloop()
