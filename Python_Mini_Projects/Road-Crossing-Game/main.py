import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

screen: Screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Welcome to Road Crossing Game")

player: Player = Player()
car_manager: CarManager = CarManager()
scoreboard: ScoreBoard = ScoreBoard()
turtle = Turtle = Turtle()


screen.listen()
screen.onkey(player.go_up, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect Collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect Successful Crossing
    if player.is_at_final_position():
        player.go_to_start()
        car_manager.leve_up()
        scoreboard.increase_level()


screen.exitonclick()

