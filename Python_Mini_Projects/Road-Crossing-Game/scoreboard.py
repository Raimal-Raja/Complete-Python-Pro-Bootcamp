from turtle import Turtle

FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-50, 260)
        self.level = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f'Level: {self.level}', align='left',font=FONT)
    def increase_level(self):
        self.level += 1
    def game_over(self):
        self.goto(0,0)
        self.write('GAME OVER', align='left',font=FONT)


