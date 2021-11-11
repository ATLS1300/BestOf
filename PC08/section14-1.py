#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 2 2021


    OBJECTIVE - To get one of the bugs to leave the water by getting the turtles to 
    chase the bugs. When this occurs, "You win!" is printed in the command line.
    
    RULES - To win, the player has to click on the bugs repeatedly until their 
    random movement eventually results in one of the bugs leaving the water. 
    This appears as if the turtles are chasing the bugs.

    CHALLENGE - The player has to get one of the bugs out of the water.
    
    INTERACTIONS - The player is clicking to direct the turtle to the bug. 

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

panel.bgcolor("OliveDrab1") # setting panel background color


# ======================== DEFINING VARIBLES ================================
running = True # variable for while loop, updates the panel animations
bugRunning = True # variable that determines whether the bugs are moving or stopped

fence = turtle.Turtle() # called fence to represent it marking the boundary the bugs must cross

bugShape = "circle" # shape of the bugs
bugColor = "khaki" # color of the bugs
bugSize = 2 # size of the bugs
bugLocation = (0,90) # location of the bugs

# ======================== CREATING WATER ====================================

# setting up the fence turtle and moving it into place
fence.pensize(10)
fence.color("DeepSkyBlue")
fence.up()
fence.goto(-300,300)
fence.setheading(0)
fence.down()

# for loop that draws the water the turtles and bugs start in 
fence.begin_fill()
for i in range (4):
    fence.forward(600)
    fence.right(90)    
fence.end_fill()
    
# ============================ CREATING CLASSES ==============================

class Frank:
    
    def __init__(self):
        
        self.turtFrank = turtle.Turtle() # turtle that moves when clicked, named Frank
            
        # making Frank (the turtle)
        self.turtFrank.shape("turtle") # making Frank turtle shaped 
        self.turtFrank.color("DarkOliveGreen") # making Frank green 
        self.turtFrank.turtlesize(5) # making Frank larger
        self.turtFrank.up()
                
        panel.update()
        
    # ========================== TURTLE METHODS ==============================
        
        # Frank's movement setup, referenced from Dr. Z's "interactionExample.py"
    def turtleMove(self,x,y):
        '''Moves the turtle to where the user clicks each time the user clicks'''  
        self.turtFrank.goto(x,y) # goes to the area where the user clicked
        self.turtFrank.right(x) # turns a little
        panel.update()

class Bug(Frank):
        
    def __init__(self, bugShape, bugColor, bugSize, bugLocation):
        
        super().__init__()
        
        global bugRunning
        self.bug = turtle.Turtle() # bug that moves to a random location when clicked
        self.panel = turtle.Screen()

        self.bug.shape(bugShape) # setting bug shape
        self.bug.color(bugColor) # setting bug color
        self.bug.turtlesize(bugSize) # changing bug size
        self.bug.up()
        self.bug.goto(bugLocation) # moving bug away from turtle for start
        
        self.bug.onclick(self.bugMove) # calling the function with onclick for user interaction
        
        panel.update()
    
    # =========================== BUG METHODS ================================
    # bug's movement setup, referenced from Dr. Z's "scopePractice.py"
    def bugMove(self,x,y): 
        '''Moves the bug to a random spot when clicked on'''
        if self.bug.xcor()-30 < x < self.bug.xcor()+30: # determines whether user clicks within 10 pixels of bug
            # if the user clicks, the bug goes to a random set of coordinates within range
            self.bug.goto(randint(-400,400), randint(-400,400)) # referenced from https://stackoverflow.com/questions/55439167/how-to-send-turtle-to-random-position
            self.turtleMove(x,y) # reference from Dr. Z and Apoorva Kanekal

            panel.update()
    
# ============================== CREATING BUGS ===============================

yellowBug = Bug(bugShape,bugColor,bugSize,bugLocation) # a yellow bug 
orchidBug = Bug(bugShape, "DarkOrchid1",bugSize, (-100,100)) # a purple bug 
pinkBug = Bug(bugShape, "LightPink", bugSize, (60,0)) # a pink bug

bugList = [yellowBug, orchidBug, pinkBug] # a list of the bugs for for loop

for bugs in bugList:
    # this for loop goes through the list of bugs, checking to see when one has crossed
    if -300 < bugs.bug.xcor() < 300 or -300 < bugs.bug.ycor() < 300:
    # if the bug's xpos or ypos are less than -300 or greater than 300, player wins
        print("You won!") # prints win message in command line
        
# TODO: use an if else statement to get the bugs to stop when their out of the water? 
# TODO: use a turtle to create a "win screen" (turtle.write()?) 

# ============================ CLEAN UP ======================================

while running: 
    # draws down everything thats happening
    panel.update()
    
turtle.mainloop() # cleanup/ allows user interactivity


