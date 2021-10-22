#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 09:48:10 2021

@author: 
Description: The player will act as a nervous pumpkin and make it to the exit of the corn maze before it gets dark
out. If they make it to the exit, they win! The pumpkin is wiggling because he is nervous! 

Friend's Feedback (XX): She really enjoyed playing the maze game and liked how it was related to 
Halloween. She didn't love how when you messed up, the lines would overlap eachother and get a little confusing.
She thinks it would be cool if there was a timer function that could say if you won or lost by making it in time.
"""

import turtle, random

# ================ LIBRARY SETTINGS SETUP =========================
turtle.colormode(255) # accept 0-255 RGB values
turtle.tracer(0) # turn off turtle's animation

panel = turtle.Screen()
w = 600
h = 600
panel.setup(width=w, height=h)


# ================ VARIABLE DEFINITION & SETUP =========================
#define turtle objects, variables, etc. here!
mazeImg = ("maze.gif")
panel.bgpic(mazeImg) #set maze as background pic

pumpkin = turtle.Turtle() #name turtle pumpkin
pumpkinImg = ("pumpkin.gif") #name pumpkin gif

pumpkin.pencolor("OrangeRed") #set pen color as orange 
pumpkin.pensize(4)

panel.addshape(pumpkinImg) # save the gif to panel 
pumpkin.shape(pumpkinImg)  # set turtle as the pumpkin gif 

pumpkin.up()
pumpkin.goto(-286,-238) #start pumpkin at beginning of maze 
pumpkin.down()

running = True      

# ================ FUNCTION DEFINITION =========================
def nextSpot(x,y): 
    '''When the user clicks next location, pumpkin moves there'''
    pumpkin.goto(x,y) # go to the click location
     

def wiggle(x=3,y=3): #optional parameters
    '''makes pumpking wiggle like it is nervous'''
    pumpkin.forward(x)
    panel.update()
    pumpkin.backward(y)


# ================ ANIMATION LOOP =========================
panel.onclick(nextSpot) # when you click location, move the turtle there
panel.listen() 

while running: 
    wiggle(x=3,y=3)
    
    
    # call functions and conditional statement to stop loop (if desired) 
      
    panel.update() # update the window with everything drawn in a single frame
    
# ================ CLEANUP =========================
turtle.mainloop()  # allows for user interactions; handles cleanup
