from turtle import Turtle
import random
tim = Turtle()

tim.shape('turtle')

# for _ in range(4):
#     tim.forward(50)
#     for _ in range(2):
#         tim.right(45)
#         tim.forward(50)
#     tim.right(90)
#

# num_sides = 10

turtle_colors = [
    "aliceblue", "antiquewhite", "aqua", "aquamarine", "azure",
    "beige", "bisque", "black", "blanchedalmond", "blue", "blueviolet",
    "brown", "burlywood", "cadetblue", "chartreuse", "chocolate",
    "coral", "cornflowerblue", "cornsilk", "crimson", "cyan",
    "violet", "wheat", "white", "whitesmoke", "yellow", "yellowgreen"
]
def draw_Shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n  in range(3, 10):
    tim.color(random.choice(turtle_colors))
    draw_Shape(shape_side_n)