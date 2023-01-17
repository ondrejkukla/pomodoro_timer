import math
from tkinter import *

# ----- CONSTANTS -----
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checkmark = ""
timer = None

# ----- TIMER RESET -----


def time_reset():
    global reps
    window.after_cancel(timer)
    reps = 0
    label_check.config(text="")
    label_timer.config(text="Timer")
    canvas.itemconfig(timer_text, text="25:00")

# ----- TIMER MECHANISM -----


def current_timer():
    global reps, checkmark
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_min = LONG_BREAK_MIN * 60
    work_min_sec = WORK_MIN * 60
    reps += 1
    if reps % 2 != 0:
        countdown(int(work_min_sec))
        label_timer.config(text="Work")
    elif reps % 8 == 0:
        countdown(int(long_break_min))
        label_timer.config(text="Break")
        label_check.config(text="")
        checkmark = ""
    elif reps % 2 == 0:
        countdown(int(short_break_sec))
        label_timer.config(text="Break")
        checkmark += "✓"
        label_check.config(text=checkmark)


# ----- COUNTDOWN MECHANISM -----


def countdown(time):
    global timer
    minutes = math.floor(time / 60)
    seconds = time % 60
    if len(str(seconds)) < 2:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if time > 0:
        timer = window.after(1000, countdown, time - 1)
    if time == 0:
        current_timer()


# ----- UI SETUP -----


window = Tk()
window.title("Pomodoro app")
window.config(padx=20, pady=20, bg="white")

label_timer = Label(text="Timer", font=("Courier", 40, "bold"), fg="black", bg="white")
label_timer.grid(row=0, column=1)

button_start = Button(text="Start", highlightthickness=0, command=current_timer)
button_start.grid(row=2, column=0)

canvas = Canvas(width=200, height=224, highlightthickness=0, bg="white")
photo_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=photo_image)
timer_text = canvas.create_text(100, 135, text=f"25:00", font=("Courier", 30, "bold"))
canvas.grid(row=1, column=1)

button_reset = Button(text="Reset", highlightthickness=0, command=time_reset)
button_reset.grid(row=2, column=2)

label_check = Label(fg=GREEN, bg="white")
label_check.grid(row=3, column=1, pady=5)
window.mainloop()
