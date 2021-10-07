#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: 
Author: 
EDITED BY: 
October 5th, 2021
Art description: There was no original description here, so I added this in. 
This is a piece where Jeff Bezos points his magic lollipop wand at people to make them rich.
Hopefully he is aiming at you ;)
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) 

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======
#go to start position and set pensize
turtle.up()
turtle.goto(25,115)
turtle.pensize(5)
turtle.color("chartreuse2") #set turtle color. moved up for organization

#define variables for right side of glasses
rightForward = 30
rightAngle = 90
rightforwardA = 17
repeat = 2

#create right side of glasses
turtle.begin_fill()
turtle.down()
for i in range(repeat):
    turtle.forward(rightForward)
    turtle.left(rightAngle)
    turtle.forward(rightforwardA)
    turtle.left(rightAngle)
turtle.end_fill()

#create glasses bridge
turtle.up()
turtle.goto(35,120)
turtle.down()
turtle.right(180) #changed turn to 180 to offset extra left turn in for loop
turtle.forward(30)
turtle.up()

#define variables for left side of glasses
forwardB = 15
forwardC = 45
angleB = 90 #turns turtle
repeat = 2 #same as on right side

#create left side of glasses
turtle.left(90) #moved this up to make for loop easier to read
#deleted color change since color stays the same
turtle.begin_fill()
turtle.down()
for i in range (repeat):
    turtle.forward(forwardB)
    turtle.right(angleB)
    turtle.forward(forwardC)
    turtle.right(angleB)
turtle.end_fill()
turtle.up()

#draw white part of wand
turtle.goto(70,-90)
turtle.pensize(10)
turtle.left(150) #consolidated left into 150 degrees instead of two lines of 90 and 60
turtle.color("azure")
turtle.down()
turtle.forward(100)
turtle.up()

#create pink circle part of wand
turtle.color("DeepPink1")
turtle.begin_fill()
turtle.right(60)
turtle.forward(30)
turtle.down()
turtle.circle(50)
turtle.end_fill()
turtle.color("DarkOrange")
turtle.up()

#create variables for movement and angles
angleA = 45
forwardA = 250
repetitions = 8

#position turtle to go in correct direction at right location
turtle.forward(200)
turtle.left(120)

#create octagon
#created a for loop since code was being repeated
turtle.down()
for i in range (repetitions):
    turtle.forward(forwardA)
    turtle.left(angleA)
turtle.up()

#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
turtle.done()
'''
1. The beginning code quality of this work was ok. I didn't have any idea what the code was (no description) or what it did.
It took me a couple runs to really understand what certain sections did, and they weren't divided originally.
2. There were instances where a for loop would have been super valuable, so I made the susbsequent changes. I also
added a bunch of comments to describe what I was doing and changing in the code. 
3. I really liked the color choices the programmer used and think that embedding the color in the code
was a smart decision for this project because it makes it easier to see what section of code you are working on.
I also really liked how the original code had some instances of hard coding, particularly in the coordinates. It just makes it easy to adjust and see what is working.
'''

'''I showed this to my friend Avarie. Here is her feedback: "I enjoy the color selection of the pink, orange, and green
because it makes the piece really stand out against the light blue background.
Overall, I also find it funny and entertaining to look at."
'''
