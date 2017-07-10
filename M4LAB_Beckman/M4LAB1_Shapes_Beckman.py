# Draw a square and a triangle with the turtle pin in python
# 6/24/2017
# CTI-110 M4LAB1: Shapes
# Allie Beckman
import turtle
turtle.shape("turtle")
def square():
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.up()
    turtle.forward(70)
    turtle.down()

def triangle():
    turtle.forward(50)
    turtle.left(120)
    turtle.forward(50)
    turtle.left(120)
    turtle.forward(50)
    turtle.left(120)
    turtle.up()
    turtle.forward(70)
    turtle.down()

while True:
    square()
    triangle()
    turtle.mode("logo")
    turtle.right(90)
