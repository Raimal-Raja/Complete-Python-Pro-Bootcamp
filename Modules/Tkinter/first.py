import tkinter

window = tkinter.Tk()
window.title("This My Second GUI Program")
window.minsize(width=500, height=300)
my_label   = tkinter.Label(text="Hello Professor", font=("Arial", 24, "italic", "bold"))
# my_label.pack(side="top")
my_label.pack()

def clicked_me():
    print()
    my_label.config(text="I was clicked")

button  = tkinter.Button(text="click me", command=clicked_me)

button.pack()






# config(padx= , pady=)
# pack(side='left')
# space(x=, y=)
# grid(coloum=,row=,)



window.mainloop()