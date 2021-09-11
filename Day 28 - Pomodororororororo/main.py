import tkinter
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 



# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 != 0:  # reps 1,3,5,7
        count_down(work_sec)
        timer_label.config(text="WORK", fg=GREEN)
    elif reps == 8:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    else:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_minutes = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")

    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodororororo")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=2, row=2)

start_button = tkinter.Button(text="Start", command=start_timer)
start_button.grid(column=1, row=3)

reset_button = tkinter.Button(text="Reset")
reset_button.grid(column=3, row=3)

check_marks = tkinter.Label(text="✓", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15))
check_marks.grid(column=2, row=4)

timer_label = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
timer_label.grid(column=2, row=1)

window.mainloop()

