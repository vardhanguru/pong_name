from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score1=0
        self.penup()
        self.hideturtle()
        self.lscore=0
        self.rscore=0
        self.color("white")
        self.goto(-200,250)
        self.write(self.lscore,font=('calibri',35))
        self.goto(200, 250)
        self.write(self.rscore, font=('calibri', 35))

    def lpoint(self):
        self.lscore+=1
        self.clear()
        self.goto(-200, 250)
        self.write(self.lscore, font=('calibri', 35))
        self.goto(200, 250)
        self.write(self.rscore, font=('calibri', 35))


    def rpoint(self):
        self.rscore+=1
        self.clear()
        self.goto(200, 250)
        self.write(self.rscore, font=('calibri', 35))
        self.goto(-200, 250)
        self.write(self.lscore, font=('calibri', 35))



