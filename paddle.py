from turtle import Turtle

# Positional constants
WIDTH = 5
LENGTH = 1

class Paddle(Turtle):
    """
    Creates a new paddle object (3 coloured squares).

    - .up(): sets orientation to a 90º angle in relation to screen
    - .down(): sets orientation to a 270º angle in relation to screen
    """

    def __init__(self, position):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_wid=WIDTH, stretch_len=LENGTH)
        self.penup()
        self.goto(position)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)