import time
from turtle import Screen
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Score()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')
game = True
while game:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        scoreboard.sco = scoreboard.sco + 1
        scoreboard.clear()
        scoreboard.update()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280:
        snake.head.goto(-snake.head.xcor(), snake.head.ycor())
    if snake.head.ycor() > 280 or snake.head.ycor() < -280:
        snake.head.goto(snake.head.xcor(), -snake.head.ycor())
    for seg in snake.segment:
        if seg == snake.head:
            pass
        elif snake.head.distance(seg) < 10:
            game = False
            scoreboard.game_over()

screen.exitonclick()
