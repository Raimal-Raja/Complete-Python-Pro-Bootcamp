import turtle
import pandas as pd
screen = turtle.Screen()
screen.title("Us States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
all_states_list = data.state.to_list()

print(all_states_list)
# print(answer)

guess_list = []
n = 50
while len(guess_list) < n:
    answer = screen.textinput(title=f"{len(guess_list)}/50 Correct States", prompt="What's the next state's name").title()
    if answer in all_states_list:
        guess_list.append(answer)
        timy = turtle.Turtle()
        timy.hideturtle()
        timy.penup()
        row = data[data.state == answer]
        timy.goto(int(row.x),int(row.y))
        # timy.write(answer)

        #.item() method will extract first element
        timy.write(row.state.item())
    elif answer =='stop':
        n =0


screen.exitonclick()