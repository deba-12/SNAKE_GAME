from turtle import Turtle

FONT = ("Arial", 16, "bold")
POINT = 0
ALIGNMENT = "center"


class Score(Turtle):
    sco = POINT

    def __init__(self):
        super().__init__()
        self.color('orange')
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.update()

    def update(self):
        self.write(f"Score : {self.sco}", False, align="center", font=("Arial", 16, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.color('red')
        self.write(f"GAME OVER", False, align=ALIGNMENT, font=FONT)
