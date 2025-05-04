from tkinter import *
import requests

url = "https://api.kanye.rest"

def get_quote():
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        quote = data['quote']
        canvas.itemconfig(quote_text, text=quote)
    except requests.exceptions.RequestException as e:
        canvas.itemconfig(quote_text, text=f"Error fetching quote: {e}")
    except KeyError:
        canvas.itemconfig(quote_text, text="Error: Could not parse quote from response.")

window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
try:
    background_img = PhotoImage(file='images/background.jpg')
    canvas.create_image(150, 207, image=background_img)
except TclError:
    print("Error: 'background.jpg' not found. Please make sure the image file is in the same directory as the script.")
    # You might want to set a default background color or handle this differently

quote_text = canvas.create_text(150, 207, text="Click Kanye for Wisdom", width=250, font=('Arial', 20, "bold"), fill="white")
canvas.grid(row=0, column=0)

try:
    kanye_img = PhotoImage(file="images/kanye.png")
    kanye_btn = Button(image=kanye_img, highlightbackground=0, command=get_quote)
    kanye_btn.grid(row=1, column=0)
except TclError:
    print("Error: 'kanye.png' not found. Please make sure the image file is in the same directory as the script.")
    # You might want to create a text button as a fallback

window.mainloop()