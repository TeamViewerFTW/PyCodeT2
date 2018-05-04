import turtle
import random
R = random.random()
B = random.random()
G = random.random()

turtle.pen()
turtle.shape("train")
while True:
    turtle.pen(5)
    R = random.random()
    B = random.random()
    G = random.random()
    turtle.color(R, G, B)
    turtle.forward(100)
    turtle.backward(200)
    turtle.forward(100)
