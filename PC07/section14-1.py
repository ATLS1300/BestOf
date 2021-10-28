# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 17:08:01 2021


There's a yellow bug on the screen. When the user clicks the bug, a turtle goes 
to the bug, and the bug moves to a new spot.
"""

# importing necessary libraries
import turtle
from random import randint

# ========================== SETTINGS + SETUP ================================
turtle.tracer(0) # turn of the turtles animation

# panel setup 
panel = turtle.Screen() # panel turtle
w = 800 # width of panel
h = 800 # height of panel
panel.setup(width=w, height=h)

panel.bgcolor("DeepSkyBlue2") # setting panel background color


# ======================== DEFINING VARIBLES ================================
running = True # variable for while loop, updates the panel animations

turtFrank = turtle.Turtle() # turtle that moves when clicked, named Frank
bug = turtle.Turtle() # bug that moves to a random location when clicked

# ========================= TURTLE SETUP ======================================
# turtle (frank) setup
turtFrank.shape("turtle") # making Frank turtle shaped 
turtFrank.color("DarkOliveGreen") # making Frank green 
turtFrank.turtlesize(5) # making Frank larger
turtFrank.up()

# bug setup
bug.shape("circle") # setting bug shape
bug.color("khaki") # setting bug color
bug.turtlesize(2) # changing bug size
bug.up()
bug.goto(0,90) # moving bug away from turtle for start

# ========================== FUNCTION SETUP ==================================

# TODO: Animate turtle moving from one point to another using a while loop
# TODO: Create a win condition/add scoring of some sort

# Frank's movement setup, referenced from Dr. Z's "interactionExample.py"
def turtleMove(x,y):
    '''Moves the turtle to where the user clicks each time the user clicks'''  
    turtFrank.goto(x,y) # goes to the area where the user clicked
    turtFrank.right(x) # turns a little

# bug's movement setup, referenced from Dr. Z's "scopePractice.py"
def bugMove(x,y): 
    '''Moves the bug to a random spot when clicked on'''
    if bug.xcor()-30 < x < bug.xcor()+30: # determines whether user clicks within 10 pixels of bug
        # if the user clicks, the bug goes to a random set of coordinates within range
        bug.goto(randint(-300,0), randint(0,300)) # referenced from https://stackoverflow.com/questions/55439167/how-to-send-turtle-to-random-position
        turtleMove(x,y) # reference from Dr. Z and Apoorva Kanekal
    
# ================= FUNCTION CALLS AND CLEANUP ===============================
panel.onclick(bugMove) # calling the function with onclick for user interaction

while running: 
    # draws down everything thats happening
    panel.update()
    
turtle.mainloop() # cleanup/ allows user interactivity