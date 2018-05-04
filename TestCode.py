import turtle
while True:
    turtle.screensize(500,500)
    turtle.circle(10)
    turtle.forward(20)
    xcor = turtle.xcor()
    if xcor >= 500:
        turtle.backward(500)
