from turtle import Screen,Turtle
from ball import Ball
import time
from paddle import Paddle
from score import ScoreBoard

def check_ball_paddle_right():
   if ball.ycor() > paddle_right.ybot() and ball.ycor() < paddle_right.ytop():
      return True

def check_ball_paddle_left():
   if ball.ycor() > paddle_left.ybot() and ball.ycor() < paddle_left.ytop():
      return True

bob = Turtle()
bob.penup()
bob.penup()
bob.goto(0,300)
bob.setheading(270)
bob.pencolor("white")
for x in range(20):
   bob.pendown()
   bob.forward(20)
   bob.penup()
   bob.forward(20)

def check_paddle_ball():
   if ball.xcor() > 330 and ball.ycor() < paddle_right.ytop() and ball.ycor()>paddle_right.ybot():
      return True
   else:
      return False
score = ScoreBoard(0,0) 
score_left = ScoreBoard(-125, 250)
score_left.print_score()
score_right = ScoreBoard(125, 250)
score_right.print_score()


ball = Ball()
paddle_left = Paddle(-350,0)
paddle_right = Paddle(350 , 0)
screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=800 , height=600)
screen.listen()
screen.onkey(paddle_left.move_up,"w")
screen.onkey(paddle_left.move_down,"s")
screen.onkey(paddle_right.move_up,"Up")
screen.onkey(paddle_right.move_down,"Down")




game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor() > 290 or ball.ycor() < -290:
      ball.bounce_wall()
    if check_ball_paddle_right() and ball.xcor()>330 and paddle_right.xcor() > ball.xcor():
       ball.bounce_from_paddle()
       score_right.increase_score()
    if check_ball_paddle_left() and ball.xcor() < -330 and paddle_left.xcor() < ball.xcor():
       ball.bounce_from_paddle()
       score_left.increase_score()  
    if ball.xcor() > 450 or ball.xcor() <-450:
       score.game_over()
       break
       





screen.exitonclick()

