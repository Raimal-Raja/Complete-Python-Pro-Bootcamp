from turtle import Turtle, Screen


screen: Screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")

starting_position = [(0, 0), (-20, 0), (-40, 0)]

for position in starting_position:
    new_segment = Turtle('square')
    new_segment.color('white')
    new_segment.goto(position)

# segment_2 = Turtle("square")
# segment_2.color("white")
# segment_2.goto(-20, 0)
#
# segment_3 = Turtle('square')
# segment_3.color("white")
# segment_3.goto(-40, 0)

screen.exitonclick()

