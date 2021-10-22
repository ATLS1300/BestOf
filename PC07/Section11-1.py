#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on WHAT DAY IS IT???

@author: WHO ARE YOU??

This code creates a simple geometric design with lines and circles wherever you click. If you tap the letter c on your keyboard it chnges the fill color of the circles.
"""

import turtle
import random


# ================ LIBRARY SETTINGS SETUP =========================
turtle.colormode(255) # accept 0-255 RGB values
turtle.tracer(0) # turn off turtle's animation

panel = turtle.Screen()
w = 700
h = 500
panel.setup(width=w, height=h)
panel.bgcolor("white")

# ================ VARIABLE DEFINITION & SETUP =========================
#define turtle objects, variables, etc. here!
running = True

turtle = turtle.Turtle()

# ================ FUNCTION DEFINITION =========================
# define your functions here! Use descriptive names and don't forget 
# a docstring!

def click(x,y,c=input("what color would you like to use?")):
    """this function creates 18 lines each 20 degrees away from the next. The lines have random lengths between 10 and 50 with a blue circle of a random radius followed by another line of random length"""

    for i in range(1):
        turtle.down()
        turtle.goto(x,y)
        xx = turtle.xcor()
        yy = turtle.ycor()
        turtle.fillcolor(c)
        for i in range(18):
            xx = turtle.xcor()
            yy = turtle.ycor()
            turtle.right(20)
            turtle.forward(random.randrange(10,50))
            turtle.begin_fill()
            turtle.circle(random.randrange(5,15))
            turtle.end_fill()
            turtle.forward(random.randrange(10,50))
            turtle.up()
            turtle.goto(xx,yy)
            turtle.down()
        turtle.up()



panel.onclick(click)


# ================ ANIMATION LOOP =========================
while running:
    # call functions and conditional statement to stop loop (if desired) 
      
    panel.update() # update the window with everything drawn in a single frame
    
# ================ CLEANUP =========================
turtle.mainloop()  # allows for user interactions; handles cleanup



