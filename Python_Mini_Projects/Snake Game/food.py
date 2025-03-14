from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.speed(0)
        self.refresh()

    def refresh(self):
        """Moves the food to a random location within the screen bounds."""
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)
