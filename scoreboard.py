from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.value = 1
        self.goto(-200, 250)
        self.write(f"Level: {self.value}", align="center", font=FONT)

    def increase_score(self):
        self.value += 1

    def update_score(self):
        self.clear()
        self.goto(-200, 250)
        self.write(f"Level: {self.value}", align="center", font=FONT)
