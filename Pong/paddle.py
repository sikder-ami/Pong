from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,x):
        super().__init__()
        if x ==1:
            self.teleport(-350, 0)
        elif x==2 :
            self.teleport(350, 0)
        self.shape("square")
        self.shapesize(5, 1)
        self.penup()
        self.color("white")


    def up(self):
        self.goto(self.xcor(),self.ycor()+50)
    def down(self):
        self.goto(self.xcor(),self.ycor()-50)



