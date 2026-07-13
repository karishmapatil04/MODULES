import turtle

# Create screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create turtle
pen = turtle.Turtle()
pen.speed(5)

# Colours
colors = ["red", "blue", "green", "yellow"]

# Function to draw a petal
def petal(color):
    pen.color(color)
    pen.begin_fill()
    pen.circle(50, 60)
    pen.left(120)
    pen.circle(50, 60)
    pen.left(120)
    pen.end_fill()

# Draw colourful petals
for i in range(8):
    petal(colors[i % 4])
    pen.left(45)

turtle.done()