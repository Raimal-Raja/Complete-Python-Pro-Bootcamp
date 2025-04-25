from tkinter import *
import time
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN ="#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# Timer count down
def counter_timer(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f'0{count_min}'

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, counter_timer, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            mark += "✔️"
        tick_lable.config(text=mark)

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        counter_timer(long_break_sec)
        title_lable.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        counter_timer(short_break_sec)
        title_lable.config(text="Break", fg=PINK)
    else:
        counter_timer(work_sec)
        title_lable.config(text="Work", fg=GREEN)

def reset_timer():
    global timer, reps
    if timer:
        window.after_cancel(timer)
        timer = None
    canvas.itemconfig(timer_text, text='00:00')
    title_lable.config(text='Timer')
    tick_lable.config(text='')
    reps = 0


# display portion

window = Tk()
window.title("Pomodoro")

window.config(padx=100, pady=50, bg=YELLOW)

title_lable = Label(text="Timer", font=(FONT_NAME, 30, 'bold'), fg=GREEN, bg=YELLOW)
tick_lable = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15))
start_btn = Button(text='Start', font=FONT_NAME, highlightthickness=0, command=start_timer)
reset_btn = Button(text="Reset", font=FONT_NAME, highlightthickness=0, command=reset_timer)

canvas = Canvas(width=200, height=200, bg=YELLOW, highlightthickness=0)
try:
    tomato_img = PhotoImage(file='pngwing.png')
    canvas.create_image(100, 100, image=tomato_img)
except TclError:
    print("Error: 'pngwing.png' not found. Please make sure the image file is in the same directory.")
    # You might want to provide a fallback or handle this error differently

timer_text = canvas.create_text(100, 112, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))

title_lable.grid(column=2, row=0)
canvas.grid(column=2, row=1)
start_btn.grid(column=1, row=2)
reset_btn.grid(column=3, row=2)
tick_lable.grid(column=2, row=3)

window.mainloop()