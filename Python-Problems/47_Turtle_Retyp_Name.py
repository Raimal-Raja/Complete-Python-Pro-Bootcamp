import turtle
import time
import itertools


def type_and_erase():
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Typing Effect - Raimal Raja Kolhi")

    writer = turtle.Turtle()
    writer.speed(0)
    writer.penup()
    writer.hideturtle()

    colors = itertools.cycle(["red", "green", "blue", "yellow", "cyan", "magenta", "white"])
    name = "RAIMAL RAJA KOLHI"

    while True:
        writer.goto(-120, 0)

        # Typing effect
        for letter in name:
            writer.color(next(colors))
            writer.write(letter, font=("Arial", 28, "bold"))
            time.sleep(0.2)
            writer.forward(22)

        time.sleep(1)

        # Erasing effect
        writer.goto(-120, 0)
        for letter in name:
            writer.color("black")
            writer.write(letter, font=("Arial", 28, "bold"))
            time.sleep(0.1)
            writer.forward(22)

        writer.clear()


type_and_erase()
turtle.done()
