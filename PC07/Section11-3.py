#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 10/18/2021

@author: 

My code is an interactive activity targeted for children 3 years old and below.
The interactive "game" hopes to bring joy to babies when they use the comp-
uter mouse to click on the screen. When the screen (watering pot) is clicked,
flowers grow from grass. The activity is effortless and can easily satisfy
infants. 

I first created all of my turtles. My code has three turtles: a watering can, 
a flower, and a butterfly. The background of my code is set to green, mimicking grass. 
I created a butterflycircle call back function (that includes a parameter. 
This call back function controls how fast the butterfly moves, the direction it movies in, 
and where it is placed on the screen. This only works because the call back 
function is connected to the animation loop I created. The plant_flower function 
enables the watering can to "grow" flowers everytime the mouse clicks the screen. 
I used code from my PC06 assignment to help me create my functions. In the while loop,
I made the watering pot move back and forth quickly, as well. 
"""

import turtle
# ================ LIBRARY SETTINGS SETUP =========================
turtle.colormode(255) # accept 0-255 RGB values
turtle.tracer(0) # turn off turtle's animation

panel = turtle.Screen()
w = 700
h = 500
panel.setup(width=w, height=h)
panel.bgcolor("green")

# ================ VARIABLE DEFINITION & SETUP =========================
#define turtle objects, variables, etc. here!
running = True

# create watering can turtle 
wateringcan = turtle.Turtle()
wateringcanImg = "wateringcan.gif" # turtle library ONLY works with gifs!
panel.addshape(wateringcanImg) # save the image to the panel so it knows what to draw
wateringcan.shape(wateringcanImg) # change the turtle shape to the saved image
wateringcan.penup()
wateringcan.sety(-100) # making the turtle start higher up on the screen
wateringcan.up() 

# create flower turtle
flower = turtle.Turtle()
flowerImg = "flower.gif" # turtle library ONLY works with gifs!
panel.addshape(flowerImg) # save the image to the panel so it knows what to draw
flower.shape(flowerImg) # change the turtle shape to the saved image
flower.penup()
flower.sety(-100) 
flower.up() 

# create butterfly turtle
butterfly = turtle.Turtle()
butterflyImg = "butterfly.gif"
panel.addshape(butterflyImg) 
butterfly.shape(butterflyImg) # change the turtle shape to the saved image
butterfly.penup()
butterfly.setx(200)
butterfly.sety(200) # making the turtle start higher up on the screen
butterfly.up() 

# ================ FUNCTION DEFINITION =========================
# callback function to plant flowers
def plant_flower(x,y):
    """when screen clicked, flowers grow"""
    wateringcan.goto(x-50,y+20) # watering can is above the flower
    flower.goto(x,y)
    flower.stamp()

# function to make butterfly move     
def butterflycircle(x=3): # optional paramter
    """make butterfly move in a circle in the air"""
    butterfly.forward(x)
    butterfly.right(2*x)
    
# click to grow flowers
turtle.onscreenclick(plant_flower) #when screen clicked call back at plant_flower

# ================ ANIMATION LOOP =========================
while running: # watering can movement
    wateringcan.forward(3)
    panel.update()
    wateringcan.backward(3)
    butterflycircle(6) 
    
    panel.update() # update the window with everything drawn in a single frame
    
# ================ CLEANUP =========================
turtle.mainloop()  # allows for user interactions; handles cleanup



