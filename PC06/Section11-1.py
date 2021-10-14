#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 19:37:34 2021

@author: 
An animation where a pumpkin image is sliding from one edge of the screen to 
the other three times and then stops. Once it stops a spiderweb will stamp 
in the middle of the screen.
"""
# ========================= set up ===========================
import turtle

turtle.colormode(255)
turtle.tracer(0) # turns off turtles animation

panel = turtle.Screen()
w = 700
h = 500
panel.setup(width=w, height=h)
panel.bgcolor("black")

# ================ defining turtles, variables, & images =================
pumpkin = turtle.Turtle()
web = turtle.Turtle()
web.color("white")

step = 1 # increment of image movement
running = True # while loop conditional
crosses = 0 # number of times the image hits the right side of the screen
count = 3 # allow image to hit right side 3 times, when to stop animating
loc = [(0,-100),(0,-150),(0,-200)]
size = [100,150,200]
x = 300

# import image and set as turtle
pumpkinImg = "jackgif.gif"
panel.addshape(pumpkinImg)
pumpkin.shape(pumpkinImg) # image is now turtle shape

pumpkin.up() # not drawing anymore

# ======================== define function =======================
def slider():
    '''makes pumpkin image slide back and forth across screen 3 times then stops'''
    pumpkin.forward(step) # move image incrementally by step, or 1
    x=pumpkin.xcor() # get x position of image
    pumpkin.goto(x,-150)
    return x # return x variable to use to call function in animation
        
# # ========================== animation loop ========================
while running:
    
    x = slider() #call the function to move the image
    
    if x == -300:
        # hitting the left side of the screen and move right
        step *= -1
        
    elif x == 300:
        # hits the right side of the screen and moves left
        step *= -1
        crosses += 1 # keep track of crosses
        
    if count <= crosses: # check for goal number of crosses
        running = False 
        
    panel.update()
    
    
for i in range(10): # draws the legs of the spiderweb
    web.home()
    web.right(36 * count)
    web.forward(200)
    count += 1
for i in range(3): # draws the circles of the spiderweb
    web.up()
    web.home()
    web.goto(loc[i])
    web.down()
    web.circle(size[i])
        
# ============================ clean up ==========================
turtle.done()
