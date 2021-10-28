#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 10/19/21



This code makes a turtle wiggle randomly around the panel and the user can click
a certain position to make the turtle go there. Each mouse click stamps a turtle.
User can click a key to make it change colors and a different key to change the
thickness of the lines.

Besides color and movement, I also added a message that prints in the console
that lets user know if their click was out of bounds and that turtle has quit
wiggling. If this happens, turtle will write "ouch" next to the click location.
"""

import turtle, random

# ================ LIBRARY SETTINGS SETUP =========================
turtle.colormode(255) # accept 0-255 RGB values
turtle.tracer(0) # turn off turtle's animation
turtle.shape("turtle")

panel = turtle.Screen()
w = 700
h = 700
panel.setup(width=w, height=h)

# ================ VARIABLE DEFINITION & SETUP =========================
#define turtle objects, variables, etc. here!
running = True

# ================ FUNCTION DEFINITION =========================
# define your functions here! Use descriptive names and don't forget 
# a docstring!

# click functions require TWO parameters
def clickStamp(x,y):
    '''When the user clicks, move wiggle to click location and stamp turtle'''
    turtle.goto(x,y) # go to the click location
    turtle.stamp() # stamp turtle

# keypress functions have NO parameters
def changeTurtleColor():
    '''When use presses a key, change the color of turtle'''
    rainbow = ["violet","blue","pink","green", "yellow", "red","orange"] #list of turtle colors
    turtle.color(random.choice(rainbow)) #pick a random color to change turtle to
    
def changeTurtleThickness():
    '''When use presses a key, change the cthickness of turtle'''
    thiccc = [random.randint(-50,50),10,3,6,7,2] #list of turtle thicknesses
    turtle.width(random.choice(thiccc)) #pick a random thickness

def wiggle(): #wiggle function shows sun and wiggles happy turtle
    '''make turtle draw in a random wiggle shape'''
    for i in range(2):
        turtle.forward(random.randint(-5,5)) #move forward a random int between -5 and 5
        turtle.right(15) #right 15 degrees               
    
# ================ ANIMATION LOOP =========================
# Click interactions don't go inside the loop!

#These interactions are for the screen, NOT turtle...
panel.onclick(clickStamp)
turtle.onkey(changeTurtleColor, "c")
turtle.onkey(changeTurtleThickness, "t")


# For key presses ONLY, call BEFORE the animation loop!
panel.listen() # required to get the key press to work

# Loop is for animations
while running:
    xpos = turtle.xcor()
    ypos = turtle.ycor()
    wiggle() #call wiggle function
    
    if xpos <= -350 or ypos <= -350: #boundaries for turtle
        running = False #stop loop
        print("turtle has exited boundary, turtle has stopped wiggling")
        turtle.write("       ouch") #referenced from interactionexample.py code
          
    # call functions and conditional statement to stop loop (if desired) 
      
    panel.update() # update the window with everything drawn in a single frame
    
# ================ CLEANUP =========================
turtle.mainloop()  # allows for user interactions; handles cleanup

'''
Commenter: I thought this was really cute. I loved the stamping of the turtles.
Would it be possible for the turtle to stop moving all together once it hits a boundary?
That might make it not as messy. I loved being able to change the colors. The thicknesses
sometimes made it hard to see, but it was fun to switch between making changes.
    
'''

