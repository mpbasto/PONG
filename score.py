from turtle import Turtle


class Scoreboard(Turtle):
    """
    Score begins at 0. This object keeps track of the scores and displays it on screen.
    Score increments every time ball goes out of bounds.
    """
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.track_score()


    # Track scores
    def track_score(self):
        """Returns updated scoreboard."""
        self.goto(-100, 200)
        self.write(self.l_score, align='center', font=('Courier', 80, 'normal'))
        self.goto(100, 200)
        self.write(self.r_score, align='center', font=('Courier', 80, 'normal'))


    # Point to L paddle
    def point_l(self):
        """
        Increments score of the left paddle by 1.
        """
        self.l_score += 1
        self.clear()
        self.track_score()

    # Point R paddle
    def point_r(self):
        """
        Increments score of the right paddle by 1.
        """
        self.r_score += 1
        self.clear()
        self.track_score()
