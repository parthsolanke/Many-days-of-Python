import random
from flask import Flask
app = Flask(__name__)
NUM = random.randint(0, 9)

@app.route('/')
def home():
    return "<h1 style='text-align: center;'>Guess a number between 0 and 9</h1>"\
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'"\
                 "style='display: block; margin-left: auto; margin-right: auto;' />"
                 
@app.route('/<int:number>')
def guess(number):
    if number < NUM:
        return "<h1 style='text-align: center;'>Too low, try again!</h1>"\
                "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'"\
                     "style='display: block; margin-left: auto; margin-right: auto;' />"
    elif number > NUM:
        return "<h1 style='text-align: center;'>Too high, try again!</h1>"\
                "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'"\
                     "style='display: block; margin-left: auto; margin-right: auto;' />"
    else:
        return "<h1 style='text-align: center;'>You found me!</h1>"\
                "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'"\
                     "style='display: block; margin-left: auto; margin-right: auto;' />"

if __name__ == '__main__':
    app.run(debug=True)