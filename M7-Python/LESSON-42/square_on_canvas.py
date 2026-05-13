import turtle

# creating canvas
turtle.Screen().bgcolor("Yellow")

sc = turtle.Screen()
sc.setup(700, 700)

turtle.title("Welcome to Turtle Window")

# turtle object creation
board = turtle.Turtle()

# creating a square
for i in range(4):
	board.forward(100)
	board.left(90)

turtle.done()


