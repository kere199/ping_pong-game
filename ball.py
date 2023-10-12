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
        self.sp = 0.2



       def move(self):
        x = self.xcor()
        y = self.ycor()
        self.goto(x + self.xplus, y + self.yplus)

       def bounce_wall(self):
          self.yplus *= -1

       def bounce_from_paddle(self):
          self.xplus *= -1

       def increase_speed(self):
          if self.sp > 0.03:
            self.sp -= 0.02
          else:
             self.sp +=0
          return self.sp
          
          

          
        
