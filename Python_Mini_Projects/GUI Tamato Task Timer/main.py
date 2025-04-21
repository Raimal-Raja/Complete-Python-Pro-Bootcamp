from tkinter import *

from rdflib.tools.csv2rdf import column
from sqlalchemy.testing import force_drop_names

PINK = "#e2979c"
RED = "#e7305b"
GREEN ="#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20




# display portion

window = Tk()
window.title("Pomdoro")

window.config(padx=100,pady=50,bg=YELLOW)

title_lable = Label(text="Timer", font=(FONT_NAME, 30,'bold'), fg=GREEN, bg=YELLOW)
tick_lable = Label(text="✔️")
btn_1 = Button(text='Start', font=FONT_NAME, highlightthickness=0)
btn_2 = Button(text="Reset", font=FONT_NAME, highlightthickness=0)




canvas = Canvas(width=200, height=200, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='pngwing.png')
canvas.create_image(100,100, image= tomato_img)
canvas.create_text(86,100,text="00:00",fill="white", font=(FONT_NAME, 25, "bold"))

title_lable.grid(column=2,row=0)
canvas.grid(column=2,row=2)
btn_1.grid(column=1, row=3)
btn_2.grid(column=3, row=3)
tick_lable.grid(column=2, row=4)






window.mainloop()