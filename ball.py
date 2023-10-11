from turtle import Turtle

class Ball(Turtle):
       def __init__(self):
        super(). __init__()
        self.color("white")
        self.shape("circle")
        self.goto(0,0)
        self.penup()
        self.xplus = 10
        self.yplus = 10



       def move(self):
        x = self.xcor()
        y = self.ycor()
        self.goto(x + self.xplus, y + self.yplus)

       def bounce_wall(self):
          self.yplus *= -1
          

          
        
