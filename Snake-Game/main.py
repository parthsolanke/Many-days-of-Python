import turtle as t
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time 

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

def listen_to_controls():
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")   

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Sanke EX1")
screen.tracer(0)
is_game_on = True

listen_to_controls()
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    # collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        
    # collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or \
       snake.head.ycor() > 280 or snake.head.ycor() < -280:
           scoreboard.reset()
           snake.reset()
 
    # collision with tail
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
