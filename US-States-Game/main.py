import turtle as t
import pandas as pd

screen = t.Screen()
screen.title("U.S. States Geme")
img = "US-States-Game\data\states_img.gif"
screen.addshape(img)
t.shape(img)

data = pd.read_csv(r"US-States-Game\data\50_states.csv")
states = data["state"].to_list()

guesses = []
while len(guesses) < 50:
    ans = screen.textinput(title=f"{len(guesses)}/50 States Correct",
                           prompt="What's another state's name?").title()
    
    if ans == "Exit":
        missed_states = []
        for state in states:
            if state not in guesses:
                missed_states.append(state)
        df = pd.DataFrame(missed_states)
        df.to_csv("US-States-Game\data\states_to_learn.csv")
        break
    if ans in states:
        guesses.append(ans)
        text = t.Turtle()
        text.hideturtle()
        text.penup()
        text.goto(int(data[data.state == ans].x), int(data[data.state == ans].y))
        text.write(ans)
