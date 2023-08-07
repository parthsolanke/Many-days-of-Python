from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 17, "normal")

class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        with open("Snake-Game\data.txt", mode="r") as data:
            self.highscore = int(data.read())
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.refresh()
        
    def refresh(self):
        self.clear()
        self.write(f"SCORE: {self.score} HIGH SCORE: {self.highscore}", align=ALIGNMENT, font=FONT)
        
    def increase_score(self):
        self.score += 1
        self.refresh()
        
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("Snake-Game\data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.refresh()
        