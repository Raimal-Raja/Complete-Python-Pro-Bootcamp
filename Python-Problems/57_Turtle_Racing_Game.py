from turtle import Turtle, Screen

timy = Turtle()
screen = Screen()

# resize window screen
# screen.setup(500, 400)
screen.setup(width=500, height=400)
screen.textinput(title="Make your bet", prompt="which turtle will win the race? Enter a Color: ")


tim = Turtle()

screen.exitonclick()
