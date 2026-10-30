from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("blue")
        self.penup()
        self.hideturtle()
        self.l_score=0
        self.r_score=0
        self.update()

    def update(self):
        self.clear()
        self.goto(-100,260)
        self.write(self.l_score,align='center',font=('Arial',20,'normal'))
        self.goto(100,260)
        self.write(self.r_score, align='center', font=('Arial', 20, 'normal'))

    def gameover(self):
        self.goto(0,0)
        self.write(f'Final Score:{self.l_score}-{self.r_score}', align='center', font=('Arial', 50, 'normal'))

