from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("black")
        self.penup()
        self.dx = 10
        self.dy = 10


    def move(self):
        self.goto(self.xcor() + self.dx,
                  self.ycor() + self.dy)

    def bounce(self):
        self.dy *= -1

    def paddle_bounce(self):
        self.dx *= -1

    def reset(self):
        self.goto(0,0)
        self.paddle_bounce()


