from turtle import Screen,Turtle
from ball import Ball
import time
from paddle import Paddle

ball = Ball()
paddle_left = Paddle(-350,0)
paddle_right = Paddle(350 , 0)
screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=800 , height=600)
screen.listen()
screen.onkey(paddle_left.move_up,"Up")
screen.onkey(paddle_left.move_down,"Down")
screen.onkey(paddle_right.move_up,"w")
screen.onkey(paddle_right.move_down,"s")




game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor() > 290:
      ball.bounce_wall()




screen.exitonclick()

