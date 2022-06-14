from tracemalloc import start
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)

# initialize snake, food, and scoreboard object
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# get the screen to listen to handle events (keystrokes for this example)
screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)
    snake.move()
    scoreboard

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # detect collision with wall
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        scoreboard.reset()
        snake.reset()
    
    # detect collision with self
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
    

screen.exitonclick()