import turtle
import random
# Sets the colour
R = random.random()
B = random.random()
G = random.random()
# Prompts for the size
squareSize = int(input("What size would you like your square in pixels?: "))

turtle.pen()
turtle.shape("turtle")
while True:
    turtle.pen(5)
    R = random.random()
    B = random.random()
    G = random.random()
    turtle.color(R, G, B)
    while True:
           R = random.random()
           B = random.random()
           G = random.random()
           turtle.forward(squareSize)
           turtle.left(90)
