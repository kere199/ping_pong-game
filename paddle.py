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
        self.goto(self.x, self.ycor()+20)

    def move_down(self):
        self.goto(self.x, self.ycor()-20)