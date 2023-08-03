import turtle as t

timmy = t.Turtle(shape = "turtle")
timmy.color("green")
screen = t.Screen()

def move_forward():
    timmy.forward(10)
    
def move_backward():
    timmy.backward(10)

def turn_left():
    timmy.setheading(timmy.heading() + 10)

def turn_right():
    timmy.setheading(timmy.heading() - 10)
    
def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()
    
screen.listen()
# sendig function as parameter to another fn dont end with parentheses
screen.onkey(move_forward, key="w")
screen.onkey(move_backward, key="s")
screen.onkey(turn_left, key="a")
screen.onkey(turn_right, key="d")
screen.onkey(clear, key="c")
screen.exitonclick()