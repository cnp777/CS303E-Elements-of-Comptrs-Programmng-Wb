# File: PuertoRicoFlag.py
# Student: Clara Torslov
# UT EID: ct32699
# Course Name: CS303E
# 
# Date: April 29, 2022
# Description of Program: Using Turtle Graphics to draw the Puerto Rican flag
import turtle

myBlue = '#00205B'
myRed = '#EF3340'
myWhite = '#FFFFFF'


def drawRectangle(ttl, x, y, width, height):
    """Function to draw a rectangle. Takes parameters of the coordinates of the top left corner (x,y), width and height."""
    ttl.penup()
    ttl.goto(x, y)  # go to starting point
    ttl.setheading(0)  # turtle direction: east
    ttl.pendown()  # start drawing
    for count in range(2):
        ttl.forward(width)  # draw sides
        ttl.right(90)  # turn 90 degrees
        ttl.forward(height)  # draw ends
        ttl.right(90)  # turn 90 degrees
    ttl.penup()  # end drawing


def drawTriangle(ttl, x, y, length, direction, color=None):
    """Function to draw a triangle. Takes in parameters of the coordinates of the top left corner (x,y),
    length of the sides (triangle is equilateral) and direction."""
    ttl.penup()
    ttl.goto(x, y)
    ttl.setheading(direction)
    ttl.pendown()  # start drawing
    for count in range(3):
        ttl.right(120)  # as it's a equilateral triangle
        ttl.forward(length)  # draw sides of triangle
    if color != None:
        ttl.fillcolor(color)
    ttl.penup()


def drawStar(ttl, x, y, length):
    ttl.penup()
    ttl.pencolor(myWhite)
    ttl.goto(x, y)  # staring point
    ttl.setheading(0)
    ttl.pendown()
    angle = 140
    for count in range(5): # Make 5 "legs"
        ttl.forward(length // 2)
        ttl.right(angle)
        ttl.forward(length // 2)
        ttl.right(72 - angle)
    ttl.penup()


def drawPRFlag():
    flag = turtle.Turtle()
    flag.speed(10)

    # Step 1: Draw one big red rectangle (the background)
    flag.fillcolor(myRed)
    flag.begin_fill()
    drawRectangle(ttl=flag, x=0, y=400, width=600, height=400)
    flag.end_fill()

    # Step 2: Draw the white rectangles (on top of the red background)
    flag.fillcolor(myWhite)
    flag.begin_fill()
    drawRectangle(flag, 0, 320, 600, 80)
    flag.end_fill()

    flag.begin_fill()
    drawRectangle(flag, 0, 160, 600, 80)
    flag.end_fill()

    # Step 3: Draw the blue triangle
    flag.fillcolor(myBlue)
    flag.begin_fill()
    drawTriangle(flag, 0, 400, 400, 90)
    flag.end_fill()

    # Step 4: Draw the star
    flag.fillcolor(myWhite)
    flag.begin_fill()
    drawStar(ttl=flag, x=150, y=225, length=100)
    flag.end_fill()

    turtle.done()


# Execute drawing
drawPRFlag()
