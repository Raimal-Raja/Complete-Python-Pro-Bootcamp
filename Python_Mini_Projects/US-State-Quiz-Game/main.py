import turtle
import pandas as pd
screen = turtle.Screen()
screen.title("Us States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer = screen.textinput(title="Guess the State", prompt="What's the next state's name")
print(answer)
value = pd.read_csv("50_states.csv")
screen.exitonclick()