from turtle import Turtle
import random
tim = Turtle()

color = [
    "black", "blue", "blueviolet", "brown", "chocolate",
    "coral", "cornflowerblue", "crimson", "violet"
]

direction =[0,90, 180, 270]
tim.shape('turtle')

for _ in range(100):
    tim.color(random.choice(color))
    tim.speed(30)
    tim.pensize(10)
    tim.forward(30)
    tim.setheading(random.choice(direction))
