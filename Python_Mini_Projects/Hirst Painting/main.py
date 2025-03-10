import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.speed('fast')
tim.penup()
color_list = [
    (30, 12, 8), (40, 15, 10), (50, 18, 12), (60, 20, 14),  # Dark reds
    (10, 30, 8), (15, 40, 10), (18, 50, 12), (20, 60, 14),  # Dark greens
    (8, 12, 30), (10, 15, 40), (12, 18, 50), (14, 20, 60),  # Dark blues
    (30, 10, 30), (40, 15, 40), (50, 18, 50), (60, 20, 60),  # Dark purples
    (30, 30, 10), (40, 40, 15), (50, 50, 18), (60, 60, 20),  # Dark yellows
    (30, 10, 15), (40, 15, 20), (50, 18, 25), (60, 20, 30),  # Dark pinks
    (10, 30, 15), (15, 40, 20), (18, 50, 25), (20, 60, 30),  # Dark teals
    (12, 24, 30), (24, 36, 40), (36, 48, 50), (48, 60, 60),  # Dark cyan shades
    (30, 20, 10), (40, 30, 15), (50, 40, 20), (60, 50, 25),  # Dark oranges
    (20, 10, 30), (30, 15, 40), (40, 18, 50), (50, 20, 60)   # Dark violets
]


tim.setheading(225)
tim.forward(200)
tim.setheading(0)
number_of_dots = 80
for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(30)

    if dot_count%10 ==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(300)
        tim.setheading(0)



screen = t.Screen()
screen.exitonclick()