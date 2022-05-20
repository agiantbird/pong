import turtle
import os

window = turtle.Screen()
window.title("Pong by agiantbird")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
    # lowercase t turtle for module
    # capital T Turtle for class in module
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
            #x coord, y coord
paddle_a.goto(-350, 0)

# Paddle B
    # lowercase t turtle for module
    # capital T Turtle for class in module
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
            #x coord, y coord
paddle_b.goto(350, 0)

# Paddle C
    # lowercase t turtle for module
    # capital T Turtle for class in module
paddle_c = turtle.Turtle()
paddle_c.speed(0)
paddle_c.shape("square")
paddle_c.color("white")
paddle_c.shapesize(stretch_wid=1, stretch_len=5)
paddle_c.penup()
            #x coord, y coord
paddle_c.goto(0, 260)

# Paddle D
    # lowercase t turtle for module
    # capital T Turtle for class in module
paddle_d = turtle.Turtle()
paddle_d.speed(0)
paddle_d.shape("square")
paddle_d.color("white")
paddle_d.shapesize(stretch_wid=1, stretch_len=5)
paddle_d.penup()
            #x coord, y coord
paddle_d.goto(0, -260)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.color("white")
ball.shape("square")
ball.penup()
            #x coord, y coord
ball.goto(0, 0)
# d = delta; might have to play with these numbers
ball.dx = 2
ball.dy = -2

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

def paddle_c_left():
    x = paddle_c.xcor()
    x -= 20
    paddle_c.setx(x)

def paddle_c_right():
    x = paddle_c.xcor()
    x += 20
    paddle_c.setx(x)

def paddle_d_left():
    x = paddle_d.xcor()
    x -= 20
    paddle_d.setx(x)

def paddle_d_right():
    x = paddle_d.xcor()
    x += 20
    paddle_d.setx(x)


# Keyboard binding
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_c_left, "a")
window.onkeypress(paddle_c_right, "d")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")
window.onkeypress(paddle_d_left, "Left")
window.onkeypress(paddle_d_right, "Right")




#Main game loop
while True:
    # animate whole game
    window.update()
    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")


    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collision
    # right paddle
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        os.system("afplay bounce.wav&")

    # left paddle
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        os.system("afplay bounce.wav&")
