# Draw a snowflake with the turtle tool in python
# 6/24/2017
# CTI-110 M4LAB3: Snowflake
# Allie Beckman

#turtle starting variables
import turtle
t=turtle.Turtle()
t.pensize(3)
t.setpos(0, 0)
t.speed(10)
#variables for the starting color of the turtle
counter = 0
r = 0.2
g = 0.05
b = 0.45
nOne = 0
nTwo = 6
color = (r, g, b)
#function to control the turtle based on how large the flake will be
#d stands for distance. a stands for angle
def flake(d, a):
    for r in range(d):
        t.forward(d)
        t.left(a)
        d = d-1
    t.setpos(0, 0)
    t.left(60)
#functions for the red green and blue variables of the pen color
#function red
def getR(nOne, r):
    if nOne <= 5:
        r = round((r+0.1), 2)
    elif nOne >= 6:
        r = round((r-0.1),2)
    return (r)
#function green
def getG(nOne, g):
    if nOne <= 5:
        g = round((g+0.02), 2)
    elif nOne >= 6:
        g = round((g-0.02), 2)
    return (g)
#function blue
def getB(nOne, b):
    if nOne <= 5:
        b = round((b+0.05), 2)
    elif nOne >= 6:
        b = round((b-0.05), 2)
    return (b)
#continues to draw the snowflake
while True:
    #set color
    t.pencolor(color)
    #if else statements to control the size of each flake
    #Once the last of the largest flakes are drawn it starts over
    if counter < 3:
        flake(30, 30)
    elif counter < 9:
        flake(60, 30)
    elif counter < 15:
        flake(80, 30)
    else:
        counter = 0
    counter = counter + 1
    #if else statements controlled by two counter numbers (nOne and nTwo)
    #without these number constraints the r g b numbers would become too large
    #and result in an error.
    #Once nOne has gone past 5 the r g b variables need to be lowered to avoid
    #error. nTwo counts down to insure the same value was subtracted for continued
    #looping.
    if nOne <= 5:
        r = getR(nOne, r)
        g = getG(nOne, g)
        b = getB(nOne, b)
        color = (r, g, b)
        nOne = nOne+1
    elif nOne >= 6:
        r = getR(nOne, r)
        g = getG(nOne, g)
        b = getB(nOne, b)
        color = (r, g, b)
        nTwo = nTwo-1
        if nTwo <= 0:
            nOne = 0
            nTwo = 6
