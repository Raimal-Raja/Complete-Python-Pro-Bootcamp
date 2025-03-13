import turtle
from turtle import Turtle, Screen
import random
from typing import List

timy = Turtle()
screen = Screen()

is_race_on = False
# resize window screen
# screen.setup(500, 400)
screen.setup(width=500, height=400)
userBet = screen.textinput(title="Make your bet", prompt="which turtle will win the race? Enter a Color: ")
colors = ['red', 'orange', 'yellow', 'green', 'purple']
y_positions: list[int] = [-70, -48, -18, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 5):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-220, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if userBet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == userBet:
                print(f"You have won! The {winning_color} turtle is the winner!")

            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
