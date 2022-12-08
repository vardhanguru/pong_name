from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score

screen=Screen()
screen.bgcolor("black")
screen.title("                                                                                                       PONG GAME")
screen.setup(800,700)
screen.window_height()
screen.tracer(0)

r_paddle=Paddle((340,0))
l_paddle=Paddle((-340,0))
ball=Ball()
score=Score()





screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"W")
screen.onkey(l_paddle.go_down,"S")

game_on=True

while game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move(10, 10)
    if ball.ycor()>340 or ball.ycor()<-340:
        ball.bounce()

    if ball.xcor()>320 and ball.distance(r_paddle)<50:
        ball.bounce_x()

    if ball.xcor()<-320 and ball.distance(l_paddle)<50:
        ball.bounce_x()
    elif ball.xcor()>385:
        ball.reset_position()
        score.lpoint()
    elif ball.xcor()<-385:
        ball.reset_position()
        score.rpoint()






screen.exitonclick()