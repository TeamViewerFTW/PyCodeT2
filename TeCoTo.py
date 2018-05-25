from turtle import turtle, screen
wn = screen()
spaceship = turtle.pen()
wn.onkey(lambda: spaceship.setheading(90), 'Up')
wn.onkey(lambda: spaceship.setheading(180), 'Left')
wn.onkey(lambda: spaceship.setheading(0), 'Right')
wn.onkey(lambda: spaceship.setheading(270), 'Down')
