from tkinter import *

from click import command

from Modules.Tkinter.main import button

window = Tk()
input = Entry()

window.title("Gui Program")
window.minsize(width=500, height=300)
my_lable = Label(text="Hello", font=("Arial", 24, "bold"))
my_lable.pack()

def get_value():

    value = input.get()
    my_lable.config(text=value)


my_btn = Button(text="click me", command= get_value)

input.pack()
my_btn.pack()









window.mainloop()