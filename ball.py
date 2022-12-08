from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.ball_speed=0.1
        self.x=10
        self.y=10

    def move(self,value1,value2):
        new_x=self.xcor()+self.x
        new_y=self.ycor()+self.y
        self.goto(new_x,new_y)
    def bounce(self):
        self.y*=-1

    def bounce_x(self):
        self.ball_speed*=0.7
        self.x*=-1
    def reset_position(self):
        self.ball_speed=0.1
        self.goto(0,0)
        self.bounce_x()