import turtle
import random
R = random.random()
B = random.random()
G = random.random()

turtle.pen()
while True:
    turtle.color(R, G, B)
    turtle.forward(100)
    turtle.backward(200)
    turtle.forward(100)


