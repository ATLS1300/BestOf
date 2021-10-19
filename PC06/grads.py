#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on October 12, 2021


Animates the growth of a randomly generated vine. Then spawns a pumpkin on the vine.
A squirrel then enters from the right side of the frame and moves to the pumpkin. The squirrel
takes a bite out of the pumpkin.

Note: As shown by my pseudocode, I iniitially planned on animating the pumpkin growing, but
after running into errors and doing research online, I learned that there is no way to resize
an image with turtle. 
"""

#Import libraries
import turtle
import random

# ================ LIBRARY SETTINGS SETUP =========================
turtle.colormode(255) # accept 0-255 RGB values
turtle.tracer(0) # turn off turtle's animation

panel = turtle.Screen()
w = 700
h = 500
panel.setup(width=w, height=h)
panel.bgcolor("black")

# ================ VARIABLE DEFINITION & SETUP =========================

#Create boolean values for use in "while" loops and define variables.
twisting = True #boolean for vine growth
growing = False #boolean for pumpkin "growth" and squirrel movement

vineInc = 5 #vine movement increment
squirInc = 5 #squirrel movement increment
vineCount = 0 #starting value of counter for duration of vine animation
vineLim = 1000 #limit for vine animation
shapeColor = [(56, 163, 42), (0,0,0)] #vine color, bite color
root = (-175,0) #center of vine plant
box = [-320, -30, 145, -145] #x and y coordinates that delineate the box in which the vines are drawn
startPos = (500, 0) #starting position of squirrel and pumpkin
squirMark = 85 #x coordinate that squirrel should stop at
bitePos = (-60, -80) #position of the bite
biteRad = 40 #size of the bite


#Set up turtles
turtle.up()

vine1 = turtle.Turtle(visible = False)
vine2 = turtle.Turtle(visible = False) 
vine3 = turtle.Turtle(visible = False)
pumpkin = turtle.Turtle()
squirrel = turtle.Turtle()
bite = turtle.Turtle(visible = False)


#Import and assign images
pumpkinIMG = "Pumpkin.gif"
panel.addshape(pumpkinIMG)
pumpkin.shape(pumpkinIMG)

squirrelIMG = "Squirrel.gif"
panel.addshape(squirrelIMG)
squirrel.shape(squirrelIMG)


#Send images/turtles to their starting positions
pumpkin.goto(startPos)
squirrel.goto(startPos)

# ================ FUNCTION DEFINITION =========================
def vStart(vine, root, shapeColor):
    '''Sends vine turtles to their starting position and sets their speed and color'''
    vine.goto(root)
    vine.color(shapeColor[0])
    vine.speed(0)
    vine.down()

def plant(vine, root, vineInc, box):
    '''Instructs turtles to randomly orient and draw within a "growing box" to 
    create a jumble of vines'''
    vine.right(random.randint(-360,360))
    vine.forward(vineInc)
    xpos = vine.xcor()
    ypos = vine.ycor()
    if xpos <= box[0] or xpos >= box[1] or ypos >= box[2] or ypos <= box[3]: #determines whether the vines are outside of the "growing box"
        vine.up()
        vine.goto(root) #sends vines that went beyond the edges of the "growing box" back to the root
        vine.down()
        
def grow(root, growing):
    '''Sends pumpkin to center of plant and stamps it'''
    if growing == True:
        pumpkin.goto(root)
        pumpkin.stamp()
        panel.update()

def sneak(growing, squirInc):
    '''Moves the squirrel from right to left, stopping at the edge of the pumpkin'''
    while growing:
        squirrel.back(squirInc)
        xpos = squirrel.xcor()
        if xpos == squirMark: #checks whether the squirrel has reached the pumpkin
            growing = False #stops squirrel movement 
        panel.update()
    
def eat(bitePos, biteRad, shapeColor):
    '''Draws a filled black circle over the edge of the pumpkin to create a "bite"'''
    bite.up()
    bite.color(shapeColor[1])
    bite.goto(bitePos)
    bite.begin_fill()
    bite.down()
    bite.circle(biteRad)
    bite.end_fill()
    panel.update()

# ================ ANIMATION LOOP =========================

#Set up vines
vStart(vine1, root, shapeColor)
vStart(vine2, root, shapeColor)
vStart(vine3, root, shapeColor)

#Draw plant (vines)
while twisting:
    plant(vine1, root, vineInc, box)
    plant(vine2, root, vineInc, box)
    plant(vine3, root, vineInc, box)
    vineCount += 1 #iteration counter to stop animation loop at appropriate time
    if vineCount == vineLim:
        twisting = False
        growing = True #triggers pumpkin and squirrel movement once vine drawing is complete
    panel.update()
    
grow(root, growing)

sneak(growing, squirInc)

if squirrel.xcor() == squirMark: #draws the bite once the squirrel has reached the pumpkin
    eat(bitePos, biteRad, shapeColor)
    
# ================ CLEANUP =========================
turtle.done()



