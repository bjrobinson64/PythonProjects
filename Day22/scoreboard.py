from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.write_scores()

    def left_score(self):
        self.l_score += 1
        self.clear()
        self.write_scores()

    def right_score(self):
        self.r_score += 1
        self.clear()
        self.write_scores()
    def write_scores(self):
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("courier", 80, "normal"))
