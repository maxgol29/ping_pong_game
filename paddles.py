from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_pos):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.goto(x_pos, 0)
        self.down()
        self.up()

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
