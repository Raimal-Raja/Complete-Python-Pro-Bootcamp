# from itertools import count
from time import sleep
from tkinter import *
import time
import math

from rdflib.tools.csv2rdf import column
from sqlalchemy.testing import force_drop_names

PINK = "#e2979c"
RED = "#e7305b"
GREEN ="#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
reps = 0
timerr = None

def reset_timer():
    window.after_cancel(timerr)

# Timmer count down
def timer(count):
    # print(count)
    count_min = math.floor(count/60)
    count_sec = count % 60

    if count_sec <10:
        count_sec = f"0{count_sec}"
    if count_min <10:
        count_min = f'0{count_min}'

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timerr = window.after(1000, timer, count-1)

    else:
        start_timer()
        mark = ""
        work_sessions  =  math.floor(reps/2)
        for _ in range(work_sessions):
           mark += "✔️"
        tick_lable.config(text=mark)

def start_timer():
    # timer(2*60)
    global reps
    reps +=1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 ==0:
        timer(long_break_sec)
        title_lable.config(text="Break", fg=RED)
    elif reps % 2 ==0:
        timer(short_break_sec)
        title_lable.config(text="Break", fg=PINK)
    else:
        timer(work_sec)
        title_lable.config(text="Work", fg=GREEN)

# display portion

window = Tk()
window.title("Pomdoro")

window.config(padx=100,pady=50,bg=YELLOW)



title_lable = Label(text="Timer", font=(FONT_NAME, 30,'bold'), fg=GREEN, bg=YELLOW)
tick_lable = Label()
start_btn = Button(text='Start', font=FONT_NAME, highlightthickness=0, command= start_timer)
reset_btn = Button(text="Reset", font=FONT_NAME, highlightthickness=0, command=reset_timer)

canvas = Canvas(width=200, height=200, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='pngwing.png')
canvas.create_image(100,100, image= tomato_img)
timer_text = canvas.create_text(86,100,text="00:00",fill="white", font=(FONT_NAME, 25, "bold"))
# timer(5)
title_lable.grid(column=2,row=0)
canvas.grid(column=2,row=2)
start_btn.grid(column=1, row=3)
reset_btn.grid(column=3, row=3)
tick_lable.grid(column=2, row=4)






window.mainloop()