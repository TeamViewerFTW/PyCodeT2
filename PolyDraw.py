import turtle
import sys
sides = int(input("How many sides should this shape have?: "))
length = int(input("How long should this be?: "))



if sides == 3:
    turtle.forward(length)
    turtle.left(60)
    turtle.forward(length)
    turtle.left(60)
    turtle.forward(length)
    turtle.left(60)


elif sides == 4:
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)

elif sides == 5:
    turtle.forward(length)
    turtle.left(108)
    turtle.forward(length)
    turtle.left(108)
    turtle.forward(length)
    turtle.left(108)
    turtle.forward(length)
    turtle.left(108)
    turtle.forward(length)
    turtle.left(108)

elif sides == 6:
    turtle.forward(length)
    turtle.left(120)
    turtle.forward(length)
    turtle.left(120)
    turtle.forward(length)
    turtle.left(120)
    turtle.forward(length)
    turtle.left(120)
    turtle.forward(length)
    turtle.left(120)
    turtle.forward(length)
    turtle.left(120)

elif sides == 7:
    for i in range(1,6):
          turtle.forward(length)
          turtle.left(128.57)

    
elif sides == 8:
    for i in range(1,7):
        turtle.forward(length)
        turtle.left(135)
 

elif sides == 9:
    for i in range(1,8):
        turtle.forward(length)
        turtle.left(140)


elif sides == 10:
    for i in range(1,9):
        turtle.forward(length)
        turtle.left(144)



else:
    print("Error! Not a valid number between 3 and 10!")
    sys.exit()

            
