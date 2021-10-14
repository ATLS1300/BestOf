#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 10/13/2021

@author: 

Definition of my code:

There are two stickmen: one that walks and one that shoots a gun. The stick man 
with a gun holds a special gun that shoots multi-colored spirograph bullets.
Once the bullets hit someone, they grow in size and become extremely deadly.

"""

# ================ LIBRARY SETTINGS SETUP =========================
import turtle
import random
turtle.colormode(255) # accept 0-255 RGB values
turtle.tracer(0) # turn off turtle's animation

panel = turtle.Screen()
w = 1000
h = 500
panel.setup(width=w, height=h)
#panel.bgcolor("black")

# ================ VARIABLE DEFINITION & SETUP =========================

# Turtles
gunMan = turtle.Turtle()
stickMan = turtle.Turtle()
spirograph = turtle.Turtle()

# Changing shapes of turtles
gunIMG = "gunStickFigure.gif"
manIMG = "walkingStickMan.gif"
panel.addshape(gunIMG)
panel.addshape(manIMG)
gunMan.shape(gunIMG)
stickMan.shape(manIMG)

# Variables for spirograph
size = 4
sides = 4 
angle = 180/sides
inc = 2
numIt = int(360/inc)
innerCirc = 8
x = -165
colors = ["red", "yellow", "orange", "tomato", "orangered", "darkorange",
          "gold"]

# To be able to start the while loop, and stop it at a future time
running = True

# Setup
gunMan.up()
gunMan.goto(-200,70)
stickMan.up()
stickMan.goto(200,0)

# ================ FUNCTION DEFINITION =========================

def bullet():
    '''Draws a multi-colored spirograph bullet'''
    spirograph.goto(x,88)
    for iteration2 in range(numIt):
        spirograph.down()
        spirograph.color(random.choice(colors))
        for iteration1 in range (sides):
            spirograph.forward(size)
            spirograph.right(angle)
        spirograph.up()
        spirograph.forward(innerCirc)
        spirograph.right(inc)
    spirograph.hideturtle()

# ================ ANIMATION LOOP =========================

# Animates a bullet that fires across the panel
while running:
    spirograph.clear()
    bullet()
    
    if x >= -200: # Starts the animation
        x+=1

    if x >= 100: # Makes the bullet grow in size when it reaches the stick man
        size+=1
        innerCirc+=1
    
    if x >= 190: # Stops the animation
        stickMan.hideturtle()
        spirograph.clear()
        running = False
    panel.update() # update the window with everything drawn in a single frame
    
# ================ CLEANUP =========================


turtle.mainloop()  # allows for user interactions; handles cleanup
turtle.done()



