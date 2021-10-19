#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 11:09:09 2021

"""#inspired by boho art/simple shapes/natural colors type art and wanted to create something similar

import turtle 
import random

turtle.speed(0)
turtle.colormode(255)

#create a panel 
panel = turtle.Screen()
w = 1200 
h = 1200 
panel.setup(width=w, height=h)

#built from Dover Horesh's psuedocode/modified for sizing // rectangle 
#by assigning my line 23 of code to a turtle, I'm providing directions for this specific cursor/shape. When I call this turtle, that is the only cursor it will disturb
rect = turtle.Turtle()
rect.color(206,106,133)
rect.up()
rect.goto(-200,350)
rect.down()

#this for loop will cycle sending the turtle through these directions: 1. 400 px forward 2. turn 90 degrees 3. 700 px forward 4. turn 90 degrees twice
rect.begin_fill()
for i in range(2):
    rect.forward(400)
    rect.right(90)
    rect.forward(700)
    rect.right(90)
rect.end_fill()
rect.hideturtle()

line = turtle.Turtle()
line.color(250,162,117)
line.pensize(10)
line.up()
line.goto(-180,-346)
line.down()
line.left(90)
line.forward(691)
line.hideturtle()

line = turtle.Turtle()
line.color(250,162,117)
line.pensize(10)
line.up()
line.goto(-130,-346)
line.down()
line.left(90)
line.forward(691)
line.hideturtle()

line = turtle.Turtle()
line.color(250,162,117)
line.pensize(10)
line.up()
line.goto(-80,-346)
line.down()
line.left(90)
line.forward(691)
line.hideturtle()

line = turtle.Turtle()
line.color(250,162,117)
line.pensize(10)
line.up()
line.goto(-30,-346)
line.down()
line.left(90)
line.forward(691)
line.hideturtle()

line = turtle.Turtle()
line.color(250,162,117)
line.pensize(10)
line.up()
line.goto(20,-346)
line.down()
line.left(90)
line.forward(691)
line.hideturtle()

line = turtle.Turtle()
line.color(250,162,117)
line.pensize(10)
line.up()
line.goto(70,-346)
line.down()
line.left(90)
line.forward(691)
line.hideturtle()

line = turtle.Turtle()
line.color(250,162,117)
line.pensize(10)
line.up()
line.goto(120,-346)
line.down()
line.left(90)
line.forward(691)
line.hideturtle()

line = turtle.Turtle()
line.color(250,162,117)
line.pensize(10)
line.up()
line.goto(170,-346)
line.down()
line.left(90)
line.forward(691)
line.hideturtle()


#modified from directions for how to create half circle: https://stackoverflow.com/questions/29441237/how-to-draw-a-semicircle-in-python-turtle-only
#half circle
semiCircle = turtle.Turtle()
semiCircle.color(255,140,97)
semiCircle.up()
semiCircle.goto(-150,-350)
semiCircle.down()

semiCircle.begin_fill()
semiCircle.right(90)
semiCircle.circle(150,-180)
semiCircle.right(-90)
semiCircle.forward(300)
semiCircle.end_fill()
turtle.goto(-200,0)
semiCircle.hideturtle()

#creating smaller semi circle
semiCircleSmol = turtle.Turtle()
semiCircleSmol.color(250,162,117)
semiCircleSmol.up()
semiCircleSmol.goto(-125,-350)
semiCircleSmol.down()

semiCircleSmol.begin_fill()
semiCircleSmol.right(90)
semiCircleSmol.circle(125,-180)
semiCircleSmol.right(-90)
semiCircleSmol.forward(250)
semiCircleSmol.end_fill()
semiCircleSmol.down()
semiCircleSmol.hideturtle()

#creating star turtle

star = turtle.Turtle()
star.color(255,140,97)
star.up 
star.down()

# modified from https://www.pythonclassroom.com/turtle-graphics/turtle-graphics-with-loops#star
# this loop iterates 100 px forward and changes angle by 150 degrees 0 - 11
star.begin_fill()
for i in range(11):
    star.forward(100)
    star.left(150)
star.end_fill()

star.up()
# random.randint below will send the iteration of my star turtle to begin drawing at a random (x,y) value listed between the values below
star.goto(random.randint(-105,105),random.randint(-175,225))
star.down()
star.begin_fill()
for i in range(11):
    star.forward(100)
    star.left(150)
star.end_fill()

star.up()
# random.randint below will send the iteration of my star turtle to begin drawing at a random (x,y) value listed between the values below
star.goto(random.randint(-105,105),random.randint(-175,225))
star.down()
star.begin_fill()
for i in range(11):
    star.forward(100)
    star.left(150)
star.end_fill()

star.up()
# random.randint below will send the iteration of my star turtle to begin drawing at a random (x,y) value listed between the values below
star.goto(random.randint(-105,105),random.randint(-175,225))
star.down()
star.begin_fill()
for i in range(11):
    star.forward(100)
    star.left(150)
star.end_fill()
 
star.up()
# random.randint below will send the iteration of my star turtle to begin drawing at a random (x,y) value listed between the values below
star.goto(random.randint(-105,105),random.randint(-175,225))
star.down()
star.begin_fill()
for i in range(11):
    star.forward(100)
    star.left(150)
star.end_fill()
star.hideturtle()



