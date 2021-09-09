import tkinter
FONT = ("Arial", 24)

def calculate_km():
    km_num["text"] = int(num_entry.get()) * 1.6

window = tkinter.Tk()
window.minsize(width=350, height=200)
window.title("Convert miles to Km")

miles_label = tkinter.Label(text="Miles", font=FONT)
miles_label.grid(column=3, row=1)

km_label = tkinter.Label(text="Km", font=FONT)
km_label.grid(column=3, row=2)

equals_label = tkinter.Label(text="is equal to", font=FONT)
equals_label.grid(column=1, row=2)

km_num = tkinter.Label(text="0", font=FONT)
km_num.grid(column=2, row=2)

calc_button = tkinter.Button(text="Calculate", command=calculate_km)
calc_button.grid(column=2, row=3)

num_entry = tkinter.Entry()
num_entry.grid(column=2, row=1)


window.mainloop()
