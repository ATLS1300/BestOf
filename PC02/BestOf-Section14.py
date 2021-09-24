#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======

t=turtle.Turtle()
#Gray explosion turtle
c=t.clone()
#orange explosion turtle
d=t.clone()
#left eye laser
e=t.clone()
#right eye laser
f=t.clone()
#Red explosion

n=1
eyeLaserSize=1
o=0
#used to change the circle radius. These are initial values

eyeCircleXL=-18
eyeCircleYL=106
#Assign the values for adjusting the left eye laser

eyeCircleXR=40
eyeCircleYR=114
#Assign the values for adjusting the right eye laser

t.speed(100)
c.speed(100)
d.speed(75)
e.speed(75)
#pen speed so I don't have to wait forever 

d.reset()
d.hideturtle()
d.speed(75)
d.penup()
d.goto(-18,112)
d.pendown()
d.pencolor("red")
d.pensize(8)
d.right(23)

e.reset()
e.hideturtle()
e.speed(75)
e.penup()
e.goto(40,119)
e.pendown()
e.pencolor("red")
e.pensize(8)
e.right(20)

for i in range(20):
    d.fd(500)
    e.fd(500)
    d.undo()
    e.undo()
    eyeLaserSize=eyeLaserSize+3
    d.pensize(eyeLaserSize)
    e.pensize(eyeLaserSize)

t.reset()
t.speed(1000)
t.hideturtle()
t.penup()
t.goto(380,-380)
t.fillcolor("gray10")
t.begin_fill()
t.left(180)
t.fd(700)
t.right(105)
t.fd(100)
t.left(60)
t.fd(150)
t.right(70)
t.fd(200)
t.left(60)
t.fd(150)
t.right(75)
t.fd(200)
t.left(30)
t.fd(200)
t.goto(380,380)
t.goto(380,-380)
t.pendown()
#the gray part of the explosion

c.reset()
c.speed(1000)
c.pencolor("orange3")
c.fillcolor("orange3")
c.hideturtle()
c.penup()
c.goto(380,-380)
c.begin_fill()
c.left(180)
c.fd(500)
c.right(20)
c.fd(100)
c.right(150)
c.fd(250)
c.left(160)
c.fd(125)
c.right(40)
c.fd(280)
c.right(140)
c.fd(200)
c.left(130)
c.fd(375)
c.right(20)
c.fd(100)
c.right(150)
c.fd(250)
c.left(160)
c.fd(125)
c.right(40)
c.fd(280)
c.right(140)
c.fd(200)
c.left(165)
c.fd(80)
c.goto(380,380,)
c.goto(380,-380)
c.pendown()
#the orange part of the explosion

f.reset()
f.speed(1000)
f.pencolor("red3")
f.fillcolor("red3")
f.hideturtle()
f.penup()
f.goto(380,-380)
f.begin_fill()
f.left(180)
f.fd(230)
f.right(10)
f.fd(250)
f.right(160)
f.fd(360)
f.left(175)
f.fd(210)
f.right(30)
f.fd(250)
f.right(160)
f.fd(360)
f.left(175)
f.fd(210)
f.right(40)
f.fd(250)
f.right(160)
f.fd(360)
f.left(175)
f.fd(210)
f.right(20)
f.fd(250)
f.right(160)
f.fd(360)
f.left(175)
f.fd(210)
f.right(10)
f.fd(250)
f.right(160)
f.fd(360)
f.left(175)
f.fd(210)
f.right(30)
f.fd(250)
f.right(160)
f.fd(360)
f.left(175)
f.fd(210)
f.right(10)
f.fd(250)
f.right(160)
f.fd(360)
f.left(175)
f.fd(210)
f.goto(380,380)
f.goto(380,-380)
f.pendown()
#the red part of the explosion

f.end_fill()
c.end_fill()
t.end_fill()
#This marks the end of the explosions

timer=t.clone()
timer.goto(400,400)
timer.hideturtle()
timer.right(270)
#Timer so that the aftermath explostion doesn't appear right away.

afterMathSmoke=e.clone()
afterMathSmoke.reset()
afterMathSmoke.hideturtle()
afterMathSmoke.penup()
afterMathSmoke.pencolor(65,65,65)
afterMathSmoke.speed(200)

smokeSize=100
from random import randint
for i in range(20):
    afterMathSmoke.goto((randint(-380,380)),(randint(-380,380)))
    afterMathSmoke.dot(smokeSize)
    smokeSize=smokeSize+40
afterMathSmoke.goto(0,0)
afterMathSmoke.dot(1000)
afterMathSmoke.pendown()
#This randomly generates the smoke clounds within the bound of the frame.
#I had to look up the random library, but its nice that it's built into python!

t.clear()
f.clear()
c.clear()
d.clear()
#Clears the background stuff to try and lighten the CPU load.

hexagon=f.clone()
hexagon.reset()
hexagon.hideturtle()
hexagon.speed(100)
hexagon.penup()
hexagon.fillcolor("DarkOrchid1")
hexagon.goto(1,185)
hexagon.begin_fill()
hexagon.fd(100)
for i in range(5):
    hexagon.right(60)
    hexagon.fd(200)

hexagon.rt(60)
hexagon.fd(100)

flower=t.clone()
flower.reset()
flower.hideturtle()
flower.penup()
flower.speed(25)
flower.pensize(2)

flower.goto(0,0)
flower.pendown()
spin=160
walk=10
for i in range(75):
    flower.fd(walk)
    flower.left(spin)
    walk=(walk)+15
    if ((i % 2) == 0) :
        flower.pencolor(255,255,255)
    else:
        flower.pencolor(0,0,0)
        flower.pensize(3)
#This is for the ending flower with alternating black and white color.

hexagon.end_fill()

#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
turtle.done()
