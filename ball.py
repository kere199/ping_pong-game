from turtle import Turtle

class Ball(Turtle):
       def __init__(self):
        super(). __init__()
        self.color("white")
        self.shape("circle")
        self.goto(0,0)



       def move(self):
        self.penup()
        self.setheading(45)
        self.forward(20)
