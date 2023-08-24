from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=267)
        self.hideturtle()
        self.high_score = self.get_high_score()
        self.update_scoreboard()

    def get_high_score(self):
        with open("data.txt") as f:
            current_high_score = f.read()
        return int(current_high_score)

    def update_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score} High Score: {self.high_score}", align=ALIGNMENT,  font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode='w') as f:
                f.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()
    # def game_over(self):
    #     self.home()
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
