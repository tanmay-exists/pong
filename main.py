import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)

# Draw center line (dotted)
center_line = Turtle()
center_line.speed(0)
center_line.color("white")
center_line.penup()
center_line.goto(0, 0)
center_line.pendown()
center_line.setheading(90)  # Set heading for vertical line

# Draw dotted line using loop
gap_size = 5  # Adjust gap size for dot spacing
line_length = screen.window_height() // 2  # Half of window height
num_dots = int(line_length // gap_size) + 1  # Ensure at least one dot

for i in range(num_dots):
  y = i * gap_size - line_length  # Adjust y based on gap size and line length
  if i % 2 == 0:
    center_line.penup()
  else:
    center_line.pendown()
  center_line.goto(0, y)

for i in range(num_dots):
  y = i * gap_size - line_length  # Adjust y based on gap size and line length
  if i % 2 == 0:
    center_line.penup()
  else:
    center_line.pendown()
  center_line.goto(0, -y)

center_line.hideturtle()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect ball misses r_paddle
    if ball.xcor() > 380:
        ball.reset_ball_position()
        scoreboard.l_point()

    # Detect ball misses l_paddle
    if ball.xcor() < -380:
        ball.reset_ball_position()
        scoreboard.r_point()


screen.exitonclick()
