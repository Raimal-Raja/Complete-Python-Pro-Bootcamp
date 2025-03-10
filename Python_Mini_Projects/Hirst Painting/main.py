import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.speed('fast')
color_list = [(252, 251, 246), (253, 247, 251), (236, 251, 243)]

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