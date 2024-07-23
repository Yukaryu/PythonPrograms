from turtle import Turtle
STARTING_POS = (0, -280)
MOVE_DIS = 10
FINISH_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.reset_pos()


    def move(self):
        new_y = self.ycor() + MOVE_DIS
        self.goto(0, new_y)

    def at_fin_line(self):
        if self.ycor() > FINISH_Y:
            return True
        else:
            return False

    def reset_pos(self):
        self.setheading(90)
        self.goto(STARTING_POS)
