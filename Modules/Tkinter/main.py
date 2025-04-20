import tkinter

window = tkinter.Tk()
window.title("This My Second GUI Program")
window.minsize(width=500, height=300)
my_label   = tkinter.Label(text="Hello Professor")
my_label.pack()
window.mainloop()