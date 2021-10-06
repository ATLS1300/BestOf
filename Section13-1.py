"""
Created on Thu Sep 15 11:39:56 2020
PC04 start code

********* HEY, READ THIS FIRST **********

This pattern was inspired by a quilt square. The background is an ombre of pink squares, and in the middle of
the pattern there is a star with 12 points. Each line and fill is a random tan color that have been selected
from a list of possible colors. Everytime you run the code, the tan star will look different.

"""
import turtle
import random

turtle.colormode(255)
#turtle.tracer(0) # uncomment this line to turn off turtle's animation. You must update the image yourself using panel.update() (line 42)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 600 # width of panel
h = 600 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 


# You must make 2 turtle variables
# You must use 2 for loops (a nested for loop counts as 2!)
# You must use at least 1 random element (something from the random library)
# Don't forget to comment your code! (what does each for loop do? What does the random function you'll use do?)

# =============== ADD YOUR CODE BELOW! =================

tanPalette = [(255, 255, 255), (255, 241, 207), (255, 229, 163), (255, 216, 117), (255, 201, 64), (255, 183, 0)]
pinkPalette = [(255, 223, 215), (255, 205, 191), (255, 184, 166), (255, 165, 142), (255, 138, 107), (255, 115, 78)]

background = turtle.Turtle()
background.up()
center = turtle.Turtle()

numSize = 600

background.goto(-300, 300)
background.down()

#creates the pink squares background
for i in range(5):
    background.color(pinkPalette[i])
    background.begin_fill()
    background.fillcolor(pinkPalette[i])
    for i in range(4):
        background.forward(numSize)
        background.right(90)
    background.end_fill()
    numSize = numSize - 100
    background.up()
    background.forward(50)
    background.right(90)
    background.forward(50)
    background.left(90)
    background.down()
    
    
    
angleTri = 30

# creates star in the middle
for i in range(12):
    center.goto(0,0)
    center.down()
    center.color(random.choice(tanPalette)) # pick a random color in the tanPalette
    center.fillcolor(random.choice(tanPalette)) # pick a random color in the tanPalette
    center.begin_fill()
    center.forward(90)
    center.left(60)
    center.forward(90)
    center.left(120)
    center.forward(90)
    center.end_fill()
    center.up()
    center.right(angleTri)


#panel.update()
# =================== CLEAN UP =========================
# uncomment the line below when you are finished with your code (before you turn it in)
#background.done()
