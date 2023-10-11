from turtle import Screen,Turtle
from ball import Ball
import time

ball = Ball()
screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=800 , height=600)


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor() > 290:
      ball.bounce_wall()




screen.exitonclick()

