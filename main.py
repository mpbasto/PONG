import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Scoreboard

# Window setup
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Ping Pong Game')
screen.tracer(0)

# Start message
intro = Turtle()
intro.speed(0)
intro.color("white")
intro.shape("blank")
intro.penup()
intro.setposition(0,75)
intro.pendown()
intro.write("Press SPACE to start", align = "center", font = ("Courier", 20, "bold"))

# End message
ending = Turtle()
ending.speed(0)
ending.color('yellow')
ending.shape('blank')
ending.penup()
ending.setposition(0,0)
ending.pendown()

is_on = False # Game state

# Setting max score
max_pts = int(screen.textinput('Alright, let\'s start!',
                                  'The first player to reach the maximum points wins. Please define the maximum: '))

# Functions
def start_game():
    intro.clear()
    screen.bgpic("COURT.gif")
    global is_on
    is_on = True
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()




def game_over():
    """Ends game."""
    screen.bye()



# Setup
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scores = Scoreboard()

# Keyboard Bindings
screen.listen()
screen.onkeypress(r_paddle.up, 'Up')
screen.onkeypress(r_paddle.down, 'Down')
screen.onkeypress(l_paddle.up, 'w')
screen.onkeypress(l_paddle.down, 's')
screen.onkeypress(start_game, 'space')
screen.onkeypress(game_over, 'Escape')
screen.listen()



# Game loop
while is_on:


    # Collision detection with wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.y_bounce()


    # Collision detection with paddles
    elif ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()

    # When ball goes out of bounds & scoring
    elif ball.xcor() > 380: # R paddle miss
        ball.reset_position()
        scores.point_l()

    elif ball.xcor() < -380: # L paddle miss
        ball.reset_position()
        scores.point_r()
    global max_points
    if scores.r_score == max_pts or scores.l_score == max_pts:
        if scores.r_score == max_pts:
            is_on = False
            r_paddle.clear()
            l_paddle.clear()
            ending.write('THAT\'S THE END OF THE MATCH 🏓\nPlayer on the right wins!', align='center', font=('Courier', 18, 'bold'))
            time.sleep(1)
            ending.penup()
            ending.setposition(0, -100)
            ending.pendown()
            ending.write('Press ESC to exit game', align='center', font=('Courier', 14, 'normal'))
            screen.onkeypress(game_over, 'Escape')
            break

screen.update()

screen.exitonclick()