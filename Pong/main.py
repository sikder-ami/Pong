from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from score import Score

screen = Screen()

screen.bgcolor("aqua")
screen.setup(800,600)
screen.title("Pong")
screen.tracer(0)

paddle1= Paddle(1)
paddle2 = Paddle(2)

point = int(screen.textinput("Input", "Enter point for the game:"))
screen.listen()
screen.onkey(paddle1.up, "w")
screen.onkey(paddle1.down, "s")

screen.onkey(paddle2.up, "Up")
screen.onkey(paddle2.down, "Down")

ball=Ball()
score=Score()
speed = 0.1
game_active = True
while game_active:

    time.sleep(speed)
    ball.move()
    screen.update()


    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce()

    if (
            abs(ball.xcor() - paddle1.xcor()) < 20
            and paddle1.ycor() - 50 < ball.ycor() < paddle1.ycor() + 50
    ) or (
            abs(ball.xcor() - paddle2.xcor()) < 20
            and paddle2.ycor() - 50 < ball.ycor() < paddle2.ycor() + 50
    ):
        ball.paddle_bounce()
        if speed>0.0001:
            speed=speed*.9

    if ball.xcor()>400 :
        ball.reset()
        score.l_score+=1
        score.update()
        speed=0.1

    if ball.xcor()<-400 :
        ball.reset()
        score.r_score+=1
        score.update()
        speed=0.1
    if score.r_score==point or score.l_score==point :
        score.gameover()
        game_active=False


screen.exitonclick()

