from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.x = x
        self.y = y
        self.color("red")
        self.hideturtle()
        self.penup()
        self.goto(x,y)
        self.score = 0

    def print_score(self):
        self.clear()
        self.write(f"score:{self.score}", align= 'center' , font= ("arial",24,"normal"))


    def increase_score(self):
        self.score += 1
        self.print_score()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align= 'center' , font= ("arial",24,"normal"))