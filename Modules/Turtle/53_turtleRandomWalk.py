import turtle
from turtle import Turtle
import random
tim = Turtle()

# color = [
#     "black", "blue", "blueviolet", "brown", "chocolate",
#     "coral", "cornflowerblue", "crimson", "violet"
# ]

turtle.colormode(255)

def random_color():
    r = random.randint(0,255)
    b = random.randint(0,255)
    g = random.randint(0,255)
    random_color = (r, g, b)
    return random_color

direction =[0,90, 180, 270]
tim.shape('turtle')

for _ in range(100):
    tim.color(random_color())
    tim.speed(30)
    tim.pensize(10)
    tim.forward(30)
    tim.setheading(random.choice(direction))
