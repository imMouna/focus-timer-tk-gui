import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
ORANGE = "#FEAE6F"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    # Reset timer text to 00:00
    canvas.itemconfig(timer_text, text="00:00")
    # Reset title label to "Timer"
    title_label.config(text="Timer")
    # Rest check marks
    check_mark_label.config(text=" ")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # If it's the 8th rep
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Long Break", font=(FONT_NAME, 40, "bold"), fg=RED,)

    # If it's the 2nd/4th/6th rep
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Short Break", font=(FONT_NAME, 25, "bold"), fg=PINK,)

    # If it's the 1st/3rd/5th/7th rep
    else:
        count_down(work_sec)
        title_label.config(text="Work", font=(FONT_NAME, 40, "bold"), fg=GREEN,)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = " "
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks += "✔"
        check_mark_label.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=220, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(row=1, column=1)


# Timer Label
title_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(row=0, column=1)

# Start button
start_button = Button(text="start", font=(FONT_NAME, 13, "bold"), border=3, bg=ORANGE, command=start_timer)
start_button.grid(row=2, column=0)

# End button
reset_button = Button(text="reset", font=(FONT_NAME, 13, "bold"), border=3, bg=ORANGE, command=reset_timer)
reset_button.grid(row=2, column=2)


# Check mark Label
check_mark_label = Label(text=" ", fg=GREEN, font=(FONT_NAME, 15, "bold"))
check_mark_label.grid(row=3, column=1)

window.mainloop()