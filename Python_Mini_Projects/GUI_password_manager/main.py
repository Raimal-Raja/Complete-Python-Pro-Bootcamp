from tkinter import *
from tkinter.messagebox import showinfo, askokcancel
from random import choice, randint, shuffle
import pyperclip
import json

###################### Password Generator


def passwordGenerator():
    letters = [
        'a', 'b', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
        'z', 'A', 'B', 'C', 'D', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
        'X', 'Z'
    ]
    symbols = [
        '!', '@', '#', '$', '%', '^', '&', '*', '_', '\\', '|', '?', '`', '~'
    ]

    numbers = [
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
    ]


    password_letters = [choice(letters) for _ in range(randint(8,10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters+password_symbols+password_numbers
    shuffle(password_list)

    generated_password  = "".join(password_list)
    pyperclip.copy(generated_password)
    password.insert(0, generated_password)




####################### get values from cells

def getValue():
    email = username.get()
    password_ = password.get()
    website_ = website.get()
    new_data = {website_:{
        "Email":email,
        "Password":password_
    }}

    if len(website_) ==0:
        askokcancel(title="Warning",message="You have left website cell empty, please enter website")
    elif len(password_) == 0:
        askokcancel(title="Warning",message="You have left password empty, please enter password")
    else:
        messagebox = askokcancel(title=website_, message=f"These are the details entered: \nEmail: {email} \nPassword: {password_}")
        if messagebox:
            # try:
            #     with open("password.json", mode='r') as data_file:
            #         try:
            #             data = json.load(data_file)
            #         except json.JSONDecodeError:
            #             data = {}
            # except FileNotFoundError:
            #     data = {}
            #
            # data.update(new_data)

            with open("password.json", mode='w') as data_file:
                json.dump(new_data, data_file, indent=4)  # Correct usage of json.dump()
                password.delete(0, END)
                website.delete(0, END)


############### initializing window
window = Tk()
window.title("Password Manager")
window.config(padx=10, pady=10)

############## Entry
website = Entry(width=35)
website.focus()
username = Entry(width=35)
username.focus()
username.insert(0,"professors@gmail.com")
password = Entry(width=35)
password.focus()

############## Labels
website_label = Label(text="Website")
username_label = Label(text="Email/Username")
Password_label = Label(text="Password")

############## Buttons
add = Button(text="Add", command=getValue)
generate_password = Button(text="Generate Password", command=passwordGenerator)


############# background window
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100,image=logo_img)

#
############### Packing
canvas.grid(row=0, column=1)
############### cells
website.grid(column=1, row=1,columnspan=2)
username.grid(column=1, row=2, columnspan=2)
password.grid(column=1, row=3)

############### Label
website_label.grid(column=0, row=1)
username_label.grid(column=0, row=2)
Password_label.grid(column=0, row=3)

################## Button
generate_password.grid(column=3, row=3)
add.grid(column=1, row=4)




window.mainloop()