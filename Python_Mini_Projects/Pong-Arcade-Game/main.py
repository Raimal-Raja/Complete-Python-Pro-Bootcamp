from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Welcome to the Pong Game')


paddle: Turtle = Turtle()
paddle.shape("square")
paddle.color('white')
paddle.shapesize(stretch_wid=5, stretch_len=1)




screen.exitonclick()