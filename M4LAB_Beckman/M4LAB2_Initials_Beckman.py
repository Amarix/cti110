# Write your initials with the turtle in python
# 6/24/2017
# CTI-110 M4LAB2: Initials
# Allie Beckman
import turtle
turtle.shape("turtle")
turtle.color("blue")
turtle.pensize(5)
def nxtLtr():
    turtle.up()
    turtle.seth(0)
    turtle.forward(70)
    turtle.down()
    
def U(number):
    turtle.forward(number)
    turtle.right(30)
    turtle.forward(number)
    turtle.right(30)
    turtle.forward(number)
    turtle.right(30)
    turtle.forward(number)
    turtle.right(30)
    turtle.forward(number)
    turtle.right(30)
    turtle.forward(number)
    turtle.right(30)
    turtle.forward(number)
    
def A():
    turtle.left(120)
    turtle.forward(60)
    turtle.left(120)
    turtle.forward(30)
    turtle.left(120)
    turtle.forward(35)
    turtle.left(180)
    turtle.forward(35)
    turtle.left(60)
    turtle.forward(30)
    
def B():
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    U(6)
    turtle.left(180)
    U(8)
A()
nxtLtr()
turtle.color("purple")
B()
nxtLtr()

