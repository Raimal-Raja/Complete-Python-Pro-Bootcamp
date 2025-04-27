from tkinter import *
from tkinter.messagebox import showinfo, askokcancel


def getValue():
    email = username.get()
    password_ = password.get()
    website_ = website.get()

    messagebox = askokcancel(title=website_, message=f"These are the details entered: \nEmail: {email} \nPassword: {password_}")
    if messagebox:
        with open("password.txt",mode='w') as file:
            file.write(f"Website: {website_} Email: {email} Password: {password_} \n" )
            password.delete(0, END)
            website.delete(0,END)

# initializing window
window = Tk()
window.title("Password Manager")
window.config(padx=10, pady=10)

# Entry
website = Entry(width=35)
website.focus()
username = Entry(width=35)
username.focus()
username.insert(0,"eg; professor@gmail.com")
password = Entry(width=35)
password.focus()

# Labels
website_label = Label(text="Website")
username_label = Label(text="Email/Username")
Password_label = Label(text="Password")

# Buttons
add = Button(text="Add", command=getValue)
# getValue()

generate_password = Button(text="Generate Password")


# background window
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100,image=logo_img)

#
# # Packing
canvas.grid(row=0, column=1)
# cells
website.grid(column=1, row=1,columnspan=2)
username.grid(column=1, row=2, columnspan=2)
password.grid(column=1, row=3)

# Label
website_label.grid(column=0, row=1)
username_label.grid(column=0, row=2)
Password_label.grid(column=0, row=3)

# Button
generate_password.grid(column=3, row=3)
add.grid(column=1, row=4)




window.mainloop()