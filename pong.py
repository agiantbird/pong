import turtle

window = turtle.Screen()
window.title("Pong by agiantbird")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

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
# Ball

#Main game loop
while True:
    window.update()