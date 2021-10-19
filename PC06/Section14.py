#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 10/13/21


OUR CODE MAKES A BAT CHANGE THE COLORS
"""

import turtle

# ================ LIBRARY SETTINGS SETUP =========================
# turtle.colormode(255) # accept 0-255 RGB values
turtle.tracer(0) # turn off turtle's animation

panel = turtle.Screen()
w = 700
h = 500
panel.setup(width=w, height=h)
# panel.bgcolor("white")

# ================ VARIABLE DEFINITION & SETUP =========================
#define turtle objects, variables, etc. here!
running = True
step = 1
edgePadding = 15

# import and set image as turtle shape
batImg = "batPC06.gif" # turtle library ONLY works with gifs!
panel.addshape(batImg) # save the image to the panel so it knows what to draw
turtle.shape(batImg) # change the turtle shape to the saved image

turtle.speed(10)
turtle.up() # we're not drawing, anymore

turtle.goto(0,0)

# ================ FUNCTION DEFINITION =========================
# define your functions here! Use descriptive names and don't forget 
# a docstring!
def setBgCol(color):
    panel.bgcolor(color) 

# ================ ANIMATION LOOP =========================
while running:
    turtle.forward(step) # move bat
    xpos = turtle.xcor() # get x position
    ypos = turtle.ycor()
    
    # if bat hits right edge or top edge, then move left
    if xpos >= (w/2 - edgePadding) or ypos >= (h/2 - edgePadding):
        turtle.left(step)
        setBgCol("orange")
        panel.update()
        continue
        
    if xpos <= -w/2 - edgePadding or ypos <= (-h/2 - edgePadding):
        turtle.right(step)
        setBgCol("yellow")
        panel.update()
        continue
          
      
    panel.update() # update the window with everything drawn in a single frame
    
# ================ CLEANUP =========================
turtle.done()



