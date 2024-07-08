from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 10, 'normal')
STARTING_SCORE = 0
Y_COORDINATE = 270


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = STARTING_SCORE
        with open("data.txt", "r") as file:
            data = file.read()
            self.high_score = int(data)
        self.color("white")
        self.penup()
        self.goto(0, Y_COORDINATE)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg=f"Game Over", align=ALIGNMENT, font=FONT)

