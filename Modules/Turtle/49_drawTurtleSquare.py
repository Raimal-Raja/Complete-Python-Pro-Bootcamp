from turtle import Turtle, Screen

timmy_the_turtle: Turtle = Turtle()
timmy_the_turtle.shape('turtle')
timmy_the_turtle.color('pink')
screen: Screen = Screen()

# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)

for _ in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)

screen.exitonclick()