import turtle as t
import colorgram
import random

t.colormode(255)
tim = t.Turtle()
tim.speed('fastest')
tim.hideturtle()
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

def clickToExit():
    screen = t.Screen()
    screen.exitonclick()
    
def uTurn():
    if tim.heading() == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
    else:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(0)
        
def draw_hirst_dots():
    for dot in range(1, number_of_dots+1):
        tim.dot(20, random.choice(rgb_colors))
        if dot % 10 != 0:
            tim.forward(50)
        else:
            uTurn()

colors = colorgram.extract('Painting-Turtle\data\Hirst.jpg', 30)
rgb_colors = []
for color in colors:
    r, g, b = color.rgb.r, color.rgb.g, color.rgb.b
    rgb_colors.append((r, g, b))
    
draw_hirst_dots()
    
clickToExit()
