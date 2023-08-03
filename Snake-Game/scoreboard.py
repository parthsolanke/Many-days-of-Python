from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 17, "normal")

class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.refresh()
        
    def refresh(self):
        self.clear()
        self.write(f"SCORE: {self.score}", align=ALIGNMENT, font=FONT)
        
    def increase_score(self):
        self.score += 1
        self.refresh()
        
    def game_over(self):
        """ msg gets printed before hitting the clear method from refresh
            hence still being able to see the score """
        self.goto(0, 0)
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)
        