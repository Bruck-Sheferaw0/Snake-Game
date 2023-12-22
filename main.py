""" Python Snake Game Developed by Bruck Sheferaw """
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

# Creating new screen and creating game environment and score
screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
# Creating snake bodies and food item
seg = Snake()
food = Food()
seg.create_body()
score = Score()
# Moving snake bodies
screen.listen() # this command makes the screen catch events like onkeypress
screen.onkey(seg.up,"Up")
screen.onkey(seg.down,"Down")
screen.onkey(seg.left,"Left")
screen.onkey(seg.right,"Right")
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    seg.move_snake()
    # detect collision with food
    if seg.segment[0].distance(food) < 15:
        food.respawn()
        food.changecolor()
        score.increase_score()
        seg.extend()
    # detect collision with food
    if seg.segment[0].xcor() > 280 or seg.segment[0].xcor() < -280 or seg.segment[0].ycor() > 280 or seg.segment[0].ycor() < -280:
        game_on = False
        score.game_over()
    # detect collision with body
    for i in seg.segment:
        if i == seg.segment[0]:
            pass
        elif seg.segment[0].distance(i) < 10:
            game_on = False
            score.game_over()
    # detect higher scores to increase speed
screen.exitonclick()
