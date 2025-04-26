from tkinter import *



# initializing window
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Entry
website = Entry(width=35)
username = Entry(width=35)
password = Entry(width=35)

# Labels
website_label = Label(text="Website")
username_label = Label(text="Email/Username")
Password_label = Label(text="Password")

# Buttons
add = Button(text="Add")
generate_password = Button(text="Generate Password")


# background window
canvas = Canvas(height=200, width=200)
# logo_img = PhotoImage(file="logo.png")
# canvas.create_image(100, image=logo_img)
#
#
# # Packing
canvas.grid()
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