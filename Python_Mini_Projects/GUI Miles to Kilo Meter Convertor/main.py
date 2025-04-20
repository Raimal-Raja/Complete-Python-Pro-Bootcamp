from tkinter import  *

from nltk.sem.chat80 import borders

window = Tk()
input = Entry()

window.title("Calculator")
my_title = Label(text="Welcome to calculator", font=("Arial", 10, "bold"))
my_value = Label(text="0", font=("Arial", 10, "bold"))
window.minsize(width=300, height=150)

def calculateFunction():
    value = input.get()
    value = int(value) * 1.6
    my_value.config(text=value)

main_scale = Label(text="Miles")
primary_scale = Label(text="Kilo Meters")


my_title.grid(column=2, row=0)
input.grid(column=2, row=1)
main_scale.grid(column=3, row=1)
my_btn = Button(text="calculate", command=calculateFunction, background='green')
my_value.grid(column=2, row=4)
primary_scale.grid(column=3, row=4)
my_btn.grid(column=2, row=3)




window.mainloop()