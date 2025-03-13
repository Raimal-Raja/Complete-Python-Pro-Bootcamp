import time
from turtle import Turtle, Screen


screen: Screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)

starting_position = [(0, 0), (-20, 0), (-40, 0)]
segments = []

for position in starting_position:
    new_segment = Turtle('square')
    new_segment.color('white')
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

# segment_2 = Turtle("square")
# segment_2.color("white")
# segment_2.goto(-20, 0)
#
# segment_3 = Turtle('square')
# segment_3.color("white")
# segment_3.goto(-40, 0)
screen.update()

game_is_on = True
while game_is_on:
    for seg in segments:
        screen.update()
        seg.forward(20)
        time.sleep(1)
screen.exitonclick()

