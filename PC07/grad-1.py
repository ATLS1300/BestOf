#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on October 17, 2021


Creates "Bustin: A Ghost Hunting Game." Draws a building with 6 windows. A ghost (Image Source: https://tinyurl.com/9xn23f3t)
then appears 11 times randomly in the windows for 0.5 second each time. If the user successfully clicks
on the window that the ghost is in, they "catch" the ghost and gain 1 point. At the end, the game
prints the user's score. If they scored 7 or more, they win.

I used coolors.co when choosing my color palette to ensure users with color blindness can play "Bustin."
Also, text size exceeds accessible reading standards: https://accessibility.psu.edu/fontsizehtml/

Note: Used start_code.py for setup.
"""

#Import libraries
import turtle
import random
import time

# ================ LIBRARY SETTINGS SETUP =========================
turtle.colormode(255) # accept 0-255 RGB values
turtle.tracer(0) # turn off turtle's animation

panel = turtle.Screen()
w = 700
h = 900 #changed height so it would be "hot dog style"
panel.setup(width=w, height=h)
panel.bgcolor(18,25,43) #set bg color to Oxford Blue

turtle.title("Bustin'")
# ================ VARIABLE DEFINITION & SETUP =========================
colour = [(255,255,255),(10,10,10),(127,127,127)] #white, rich black, gray web

#Writing Variables
textSize = 50
textStyle = "Times"
textType = "normal"
over = "Game Over" #statement written on panel at end of game
winStatement = "Winner! You are spooooky good!"
loseStatement = "Too many ghosts got away! It's back to the academy for you."

#World setup variables
buildCor = [(-250,-450),(-250,350),(250,350),(250,-450)] #corner points of the building
winCor = [(-150,262.5),(50,262.5),(-150,25),(50,25),(-150,-212.5),(50,-212.5)] #starting points for drawing windows
winW = 100 #window width
winH = 150 #window height


#Variables for gameplay
hunting = True #boolean value to activate a while loop for gameplay
count = 0 #starting point for game duration tracker
inc = 1 #game duration incremement
score = 0 #score counter starting value
win = 7 #score needed to win

#Ghost movement
ghostHide = (600,0) #default position offscreen for ghost
spawn = [(-100,161.5),(100,161.5),(-100,-76),(100,-76),(-100,-313.5),(100,-313.5)] #ghost spawn points
linger = 0.5 #duration that ghost will appear on screen with each spawn
wait = 1 #time between ghost de-spawn and next ghost spawn

#Create named turtles
turtle.hideturtle()
builder = turtle.Turtle(visible=False) #draws the building and windows
ghost = turtle.Turtle()
scribe = turtle.Turtle(visible=False) #writes onscreen text

#Set up turtles
ghostIMG = "slimer.gif"
panel.addshape(ghostIMG)
ghost.shape(ghostIMG)

ghost.up()
ghost.goto(ghostHide) #send ghost to hiding spot so it cannot be seen

scribe.color(colour[0])

# ================ FUNCTION DEFINITION =========================

def winInst(winCor, winW, winH):
    '''Draws 6 windows'''
    for i in range(6):
        builder.goto(winCor[i])
        builder.down()
        builder.begin_fill()
        builder.forward(winW)
        builder.right(90)
        builder.forward(winH)
        builder.right(90)
        builder.forward(winW)
        builder.right(90)
        builder.forward(winH)
        builder.right(90)
        builder.end_fill()
        builder.up()

def build(buildCor, colour):
    '''Draws a building with 6 windows'''
    builder.up()
    builder.color(colour[2])
    builder.goto(buildCor[0])
    builder.down()
    builder.begin_fill()
    for i in range(1,4):
        builder.goto(buildCor[i])
    builder.end_fill()
    builder.up()
    builder.pencolor(colour[0])
    builder.fillcolor(colour[1])
    winInst(winCor,winW,winH)
    
def shot(x=0,y=0): #made parameters optional so function can be expanded and called without needing to pass in parameters
    '''Checks whether the user clicked on the ghost. If so, adds a point to their score'''
    ghostx = ghost.xcor()
    ghosty = ghost.ycor()
    if ghostx-50<=x<=ghostx+50 and ghosty-49<=y<=ghosty+101: #delineateas a hitbox = size of window ghost occupies
        global score
        score += 1
        return score
        
# ================ ANIMATION LOOP =========================
#World setup
build(buildCor, colour)

#Gameplay
while hunting: 
    gogoGhost = random.choice(spawn) #randomly select a spawn point
    ghost.goto(gogoGhost) #send ghost to selected spawn point
    ghost.stamp()
    panel.update()
    panel.onscreenclick(shot) #registers user's click location and uses shot() to check to see if they "captured" the ghost
    time.sleep(linger) #ghost stays at spawn point for 0.5 seconds.
    ghost.clear()
    panel.update()
    time.sleep(1) #1 second break before next spawn
    count += inc
    if count == 11:
        hunting = False #ends game after 11 ghost spawns

#End game
ghost.goto(ghostHide)
ghost.clear()
builder.clear()
panel.update() #clears screen for end-game text
scribe.write(over, align="center", font=(textStyle,textSize,textType)) #writes "Game Over"
panel.update()
print(score)
if score >= win:
    print(winStatement)
else:
    print(loseStatement)

# ================ CLEANUP =========================
turtle.mainloop()  # allows for user interactions; handles cleanup

'''
Friend Feedback:
    I love the theme of the game / the game itself!
    I think it could be improved by adding a live counter so you can see how many ghosts you caught.
'''

