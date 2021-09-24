#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 14:51:40 2021

@author: 
"""

#circles being drawn across the screen on the top and bottom rows
#squares being drawn across the screen in the middle row
#colors being chosen at random from lists of 3 rgb's per row, primary colors

import turtle, random
turtle.colormode(255)

panel = turtle.Screen()
w=600
h=600
panel.setup(width=w,height=h)
panel.bgcolor(0,0,0)
turtle.speed(10)

circle=turtle.Turtle() #turtle for controlling the first row of circles
circleColors=[(255,1,0),(255,82,82),(255,122,123)]
radius = 75
inc = 50

circle.up()
circle.goto(-220,140)
circle.pendown()

for i in range(10): #draws circles in top row and fills them as they are drawn
    circle.color(random.choice(circleColors)) #colors are chosen at random from list of rgb's above so that the colors are in a different order every time the code is ran making it generative art
    circle.begin_fill()
    circle.circle(radius)
    circle.end_fill()
    circle.forward(inc)
    
square = turtle.Turtle() # turtle for controlling the squares
squareColors= [(253,234,0),(254,245,76),(254,255,101)]
length = 125
angle= 90
square.penup()
square.goto(-370,65)
square.pendown()

for i in range(10): #repeats the squares that are being drawn in the nested loop below
    square.penup()
    square.forward(75)
    square.pendown()
    square.color(random.choice(squareColors)) #colors are chosen at random from list of rgb's above so that the colors are in a different order every time the code is ran making it generative art
    square.begin_fill()
    
    for i in range(4): #nested loop to draw each individual square
        square.forward(length)
        square.right(angle)
    square.end_fill()  
    
circle2=turtle.Turtle() # turtle for controlling second row of circles
circle2Colors=[(119,195,236),(137,207,240),(158,217,243)]
radius = 75
inc = 50

circle2.up()
circle2.goto(-220,-270)
circle2.pendown()

for i in range(10): #drawing and filling the bottom row of circles
    circle2.color(random.choice(circle2Colors)) #colors are chosen at random from list of rgb's above so that the colors are in a different order every time the code is ran making it generative art
    circle2.begin_fill()
    circle2.circle(radius)
    circle2.end_fill()
    circle2.forward(inc)

    
    
