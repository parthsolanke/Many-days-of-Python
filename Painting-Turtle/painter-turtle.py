import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.speed('fastest')
tim.shape('circle')
directions = [0, 90, 180, 270]

def clickToExit():
    screen = t.Screen()
    screen.exitonclick()

def random_color():
    r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    return (r, g, b)

def draw_spirograph(circle_radius, gap):
    for _ in range(int(360/gap)):
        tim.color(random_color())
        tim.circle(circle_radius)
        tim.setheading(tim.heading() + gap)

def random_walk(steps):
    tim.pensize(15)
    for _ in range(steps):
        tim.color(random_color())
        tim.forward(30)
        tim.setheading(random.choice(directions))

def draw_dashed_line(length):
    for _ in range(length):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()
        
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

draw_spirograph(100, 10)

clickToExit()