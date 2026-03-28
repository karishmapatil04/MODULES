import turtle

# Create screen
screen = turtle.Screen()
screen.bgcolor("lightblue")   # Background color

# Create turtle
t = turtle.Turtle()
t.speed(3)
t.pensize(3)

# --------- Draw Equilateral Triangle ---------
t.penup()
t.goto(-200, 100)
t.pendown()

t.color("black", "yellow")   # outline, fill
t.begin_fill()

for i in range(3):
    t.forward(100)
    t.left(120)

t.end_fill()

# --------- Draw Rectangle ---------
t.penup()
t.goto(0, 100)
t.pendown()

t.color("black", "green")
t.begin_fill()

for i in range(2):
    t.forward(150)
    t.left(90)
    t.forward(80)
    t.left(90)

t.end_fill()

# --------- Draw Hexagon ---------
t.penup()
t.goto(200, 100)
t.pendown()

t.color("black", "pink")
t.begin_fill()

for i in range(6):
    t.forward(70)
    t.left(60)

t.end_fill()

# Hide turtle and finish
t.hideturtle()
turtle.done()