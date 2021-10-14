#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on WHAT DAY IS IT???

@author: 

This code will display a pacman that chases a ghost to begin with and then it will be chased by the ghost, then reverse. 
"""

import turtle

# ================ LIBRARY SETTINGS SETUP =========================
turtle.colormode(255) # accept 0-255 RGB values
turtle.tracer(0) # turn off 's animation

panel = turtle.Screen()
w = 700
h = 500
panel.setup(width=w, height=h)
panel.bgcolor(0,0,0)

# ================ VARIABLE DEFINITION & SETUP =========================
#define  objects, variables, etc. here!
count = 0
limit = 5 #number of times the annimation will repeat. 

running = True

p1start = (-w/2-55,0)
 
p1end = (w/2+55)

pac1 = turtle.Turtle()
pacimg = "164447.gif" #pacman gif
panel.addshape(pacimg) 
pac1.shape(pacimg) 
pac1.penup() 

pac1.goto(p1start)

ghost = turtle.Turtle()
ghostimg = "pacmanghost1.gif"#ghost gif
panel.addshape(ghostimg)
ghost.shape(ghostimg)
ghost.up()
ghost.goto(0,0)

#horizontal = True 
#vertical = True
#cricle.showturtle()

# ================ FUNCTION DEFINITION =========================
# define your functions here! Use descriptive names and don't forget 
# a docstring!
def pac():
        p1x = pac1.xcor()#difine the pacmans x value
        pac1.forward(1)
        if p1x >= p1end:#if the x value exceeds the end of the frame then reset the pacman to its starting position.
            pac1.hideturtle()
            pac1.setpos(p1start)
            pac1.showturtle()

def ghostmove(): 
    xpos = ghost.xcor()
    ypos = ghost.ycor()
    ghost.forward(1)
    if xpos >= p1end:#preform the same operation as above. 
        ghost.hideturtle()
        ghost.setpos(p1start) 
        ghost.showturtle()
    
# ================ ANIMATION LOOP =========================
while running:
    #for i in range(1):
    for i in range(5):
        xpos = ghost.xcor()
        ypos = ghost.ycor()
        ghostmove()
        pac()
        
        if pac1.xcor() == 0: #everytime the pacman passes over (0,0) we add one to the count. 
            count += 1
            
        if count > limit:#when the count passes the limit the annimation stops. 
            running = False        
         
    panel.update() # update the window with everything drawn in a single frame
    
# ================ CLEANUP =========================
turtle.done()



