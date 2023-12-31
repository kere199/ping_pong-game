from turtle import Turtle
class Paddle(Turtle):
    def __init__(self, x,y):
        super().__init__()
        self.x = x
        self.y = y
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(x,y)



    def move_up(self):
        if self.ycor() <250:
         self.goto(self.x, self.ycor()+20)

    def move_down(self):
        if self.ycor()>-250:
          self.goto(self.x, self.ycor()-20)

    def ytop(self):
       return  self.ycor() + 60 
    
    def ybot(self):
        return self.ycor() - 60


    

