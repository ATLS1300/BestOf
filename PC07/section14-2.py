#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 10/15/2021 @ 4:15pm


Generates 4 big squares, and will divide those square into 4 smaller
squares if you click on them.
"""

import turtle

# ================ LIBRARY SETTINGS SETUP =========================
turtle.colormode(255) # accept 0-255 RGB values
turtle.tracer(0) # turn off turtle's animation

panel = turtle.Screen()
w = 550
h = 550
panel.setup(width=w, height=h)
#panel.bgcolor("black")

# ================ VARIABLE DEFINITION & SETUP =========================
#define turtle objects, variables, etc. here!
running = True
topLeft = turtle.Turtle()
topRight = turtle.Turtle()
bottomLeft = turtle.Turtle()
bottomRight = turtle.Turtle()
squareColor = ("blue","red","yellow","green")
redColors = ("lightcoral","indianred","firebrick","maroon")
blueColors = ("cornflowerblue","royalblue","darkblue","midnightblue")
yellowColors = ("lemonchiffon","khaki","goldenrod","olive")
greenColors = ("lightgreen","limegreen","seagreen","darkgreen")
squareList = (topLeft, topRight, bottomLeft, bottomRight)
topRightClones = []     #The list where the smaller clones are stored
bottomRightClones = []
topLeftClones = []
bottomLeftClones = []
sideLength = 12.8 #side of squares as a multiple of 10.
squarePosition = 512 / 4
clonePosX = squarePosition / 2
clonePosY = squarePosition / 2
k=4     #This is for generating the turtles the make the small squares

#The following determine which square was clicked. 
query_TopRight = False
query_BottomRight = False
query_TopLeft = False
query_BottomLeft = False
query_ = [query_TopRight, query_BottomRight, query_TopLeft, query_BottomLeft]

for i in range(4):
    squareList[i].shape("square")
    squareList[i].shapesize(sideLength,sideLength)
    squareList[i].color(squareColor[i])
    squareList[i].penup()
# topLeft.goto(-squarePosition/4,squarePosition)
# topRight.goto(squarePosition,squarePosition)
# bottomLeft.goto(-squarePosition,-squarePosition)
# bottomRight.goto(squarePosition,-squarePosition)
# ================ FUNCTION DEFINITION =========================
# define your functions here! Used descriptive names and don't forget 
# a docstring!

def click_coords(X,Y):
    """This function determines where on the screen the click
    occured, and then translates that to the division function
    for the square in the quadrant of the screen"""
    if X >= 0 and Y >= 0:
        query_TopRight = True
        divisionTR(query_TopRight)
    if X >= 0 and Y <= 0:
        query_BottomRight = True
        divisionBR(query_BottomRight)
    if X <= 0 and Y >= 0:
        query_TopLeft = True
        divisionTL(query_TopLeft)
    if X <= 0 and Y <= 0:
        query_BottomLeft = True
        divisionBL(query_BottomLeft)



def divisionTR(query_TopRight):
    """This function divides the top right red square into
    4 smaller squares all with shades and values of red."""
    if query_TopRight == True:
        while k != len(topRightClones):
                topRightClones.append(turtle.Turtle())
        for i in range(4):
            topRightClones[i].shape("square")
            topRightClones[i].shapesize(sideLength/2,sideLength/2)
            topRightClones[i].color(redColors[i])
                
            topRightClones[0].goto(clonePosX,clonePosY)
            topRightClones[1].goto(clonePosX * 3,clonePosY)
            topRightClones[2].goto(clonePosX,clonePosY * 3)
            topRightClones[3].goto(clonePosX * 3,clonePosY * 3)


def divisionBR(query_BottomRight):
    """This function divides the bottom right green square
    into 4 smaller squares with values and shades of green."""
    if query_BottomRight == True:
        while k != len(bottomRightClones):
            bottomRightClones.append(turtle.Turtle())
        for i in range(4):
            bottomRightClones[i].shape("square")
            bottomRightClones[i].shapesize(sideLength/2, sideLength/2)
            bottomRightClones[i].color(greenColors[i])
            
            bottomRightClones[0].goto(clonePosX, -clonePosY)
            bottomRightClones[1].goto(clonePosX * 3, -clonePosY)
            bottomRightClones[2].goto(clonePosX, -clonePosY * 3)
            bottomRightClones[3].goto(clonePosX * 3 , -clonePosY * 3)


def divisionTL(query_TopLeft):
    """This function divides the top left blue square into 
    4 smaller squares all with shades and values of blue."""
    if query_TopLeft == True:
        while k != len(topLeftClones):
            topLeftClones.append(turtle.Turtle())
        for i in range(4):
            topLeftClones[i].shape("square")
            topLeftClones[i].shapesize(sideLength/2, sideLength/2)
            topLeftClones[i].color(blueColors[i])
            
            topLeftClones[0].goto(-clonePosX, clonePosY)
            topLeftClones[1].goto(-clonePosX * 3, clonePosY)
            topLeftClones[2].goto(-clonePosX, clonePosY * 3)
            topLeftClones[3].goto(-clonePosX * 3 , clonePosY * 3)


def divisionBL(query_BottomLeft):
    """This function divides the bottom left yellow square into
    4 smaller squares with shades and values of yellow."""
    if query_BottomLeft == True:
        while k != len(bottomLeftClones):
            bottomLeftClones.append(turtle.Turtle())
        for i in range(4):
            bottomLeftClones[i].shape("square")
            bottomLeftClones[i].shapesize(sideLength/2, sideLength/2)
            bottomLeftClones[i].color(yellowColors[i])
            
            bottomLeftClones[0].goto(-clonePosX, -clonePosY)
            bottomLeftClones[1].goto(-clonePosX * 3, -clonePosY)
            bottomLeftClones[2].goto(-clonePosX, -clonePosY * 3)
            bottomLeftClones[3].goto(-clonePosX * 3 , -clonePosY * 3)
# ================ ANIMATION LOOP =========================
while running:
    topLeft.goto(-squarePosition,squarePosition)
    topRight.goto(squarePosition,squarePosition)
    bottomLeft.goto(-squarePosition,-squarePosition)
    bottomRight.goto(squarePosition,-squarePosition)
    panel.onclick(click_coords)
    # sideLength = sideLength / 2
    # squarePosition = squarePosition / 2
    
    
    # call functions and conditional statement to stop loop (if desired) 
      
    panel.update() # update the window with everything drawn in a single frame
    
# ================ CLEANUP =========================
turtle.mainloop()  # allows for user interactions; handles cleanup



