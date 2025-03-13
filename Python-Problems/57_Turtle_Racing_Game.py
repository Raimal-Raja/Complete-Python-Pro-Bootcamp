from turtle import Turtle, Screen

timy = Turtle()
screen = Screen()

# resize window screen
# screen.setup(500, 400)
screen.setup(width=500, height=400)
userBet = screen.textinput(title="Make your bet", prompt="which turtle will win the race? Enter a Color: ")
colors = ['red', 'orange', 'yellow', 'green', 'purple']
y_positions = [-70, -48, -18, 20, 50, 80]

for turtle_index in range(0, 5):
    tim = Turtle(shape='turtle')
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-220, y=y_positions[turtle_index])
screen.exitonclick()
