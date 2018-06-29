# Exercise 1 & 2
from turtle import *

def shape(sides, length, filColor, penColor):
    angle = 360 / sides
    begin_fill()
    pencolor(penColor)
    for side in range(0, sides):
        forward(length)
        right(angle)
    
    fillcolor(filColor)
    end_fill()

# Triangle
# shape(3, 100)

# Square
# shape(4, 100)

# Pentagon
# shape(5, 100)

# Hexagon 
# shape(6, 100)

# Octagon
# shape(8, 100)

# A Star
def star(length, filColor, penColor):
    begin_fill()
    pencolor(penColor)

    for side in range(0, 5):
        forward(length)
        right(144)

    fillcolor(filColor)
    end_fill()
# Circle
def circle(radius, filColor, penColor):
    begin_fill()
    pencolor(penColor)

    circle(radius)

    fillcolor(filColor)
    end_fill()
