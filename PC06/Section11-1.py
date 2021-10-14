#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on October 13, 2021

@author: 

Creates a smiling jack-o-lantern with flashing eyes
"""

import turtle, time

# ================ LIBRARY SETTINGS SETUP =========================
turtle.colormode(255) # accept 0-255 RGB values
turtle.tracer(0) # turn off turtle's animation

panel = turtle.Screen()
w = 700
h = 500
panel.setup(width=w, height=h)
panel.bgcolor("#ff7518")

# ================ VARIABLE DEFINITION & SETUP =========================
#define turtle objects, variables, etc. here!
running = True

circ = turtle.Turtle()
circ.up()
circ.goto(-25,-275)
circ.down()
circ.pensize(5)
circ.circle(295)

x2 = -150
y = -100

smile = turtle.Turtle()
smile.pensize(3)
smile.up()
smile.goto(-175,-125)
smile.down()
smile.color("#FED85B")
smile.forward(300)
smile.right(90)

for blank in range(11): #for loop creates lines in the jack o lantern's smile
        smile.up()
        smile.goto(x2,y)
        smile.down()
        smile.forward(50)
        x2 = x2 + 25

x = 175

Tri = turtle.Turtle()
Tri.up()
Tri.goto(-175,125)
Tri.down()

# ================ FUNCTION DEFINITION =========================
# define your functions here! Use descriptive names and don't forget 
# a docstring!

def Triangle():
    '''draws a triangle'''
    Tri.color("#FED85B")
    Tri.begin_fill()
    Tri.forward (50)
    Tri.left(120)
    Tri.forward(50)
    Tri.left(120)
    Tri.forward(100)
    Tri.end_fill()

def stampTriangle():
    '''stamps circle after 3 iterations'''
    for i in range(3):
        Triangle()

# ================ ANIMATION LOOP =========================
while running:
    Tri.clear()
    panel.update()
    
    stampTriangle()
    
    Tri.up()
    Tri.goto(x,125)
    Tri.down()
    
    time.sleep (0.5)
    
    x*= -1
    
    panel.update()
    
# ================ CLEANUP =========================
turtle.done()
