#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on November 3, 2021



WHAT DOES YOUR GAME DO?
    The main goal of the game is to make sure that neither of the two turtles
    touch the bottem of the screen. In order to keep the turtles from reaching
    the bottem, the player must click each turtle as they are moving in order
    to return them back to the top where they will again fall back down. The
    game will end when either of the two turtles touch the bottom of the
    screen, where the final score will be printed.

"""

import turtle
import random
# ================ LIBRARY SETTINGS SETUP =========================
turtle.colormode(255) # accept 0-255 RGB values
turtle.tracer(0) # turn off turtle's animation

panel = turtle.Screen()
w = 500
h = 600
panel.setup(width=w, height=h)

#set up images for game
background_color = (245, 245, 220)
panel.bgcolor(background_color)

# ================ VARIABLE DEFINITION & SETUP =========================
running = True
count = 0
choice = .125
# ================ FUNCTION DEFINITION =========================
# functions should go here IF they work with objects. 
# otherwise, try to include them in classes 

# ================ CLASSES =========================
class Turtles:
    def __init__(self, color_button, local_spot):
        global step
        self.color = color_button
        
        self.shape = turtle.Turtle(shape = 'turtle')
        self.shape.color(self.color)
        self.shape.shapesize(5)
        
        self.location = local_spot
        self.shape.up()
        self.shape.goto(self.location)
        
        self.shape.right(90)
        
        self.shape.onclick(self.goingTo)
        
        panel.update()
        
    def goingTo(self,x,y):
        global count
        self.shape.goto(random.randint(-250,250), 300)
        self.shape.speed(1)
        count += 1
        panel.update
        
def winOrLose():
    global running
    if Button1.shape.xcor() <= -300:
        running = False
    if Button2.shape.ycor() <= -300:
        running = False
# ================ OBJECTS =========================
# instantiate objects here
Button1 = Turtles('blue', (-200,300))        
Button2 = Turtles('green', (200,300))

# ================ ANIMATION LOOP =========================
# PRO-MOVES - can you get this while loop into a class? 
# You will have to for PC09.
while running:
    Button1.shape.forward(choice)
    Button2.shape.forward(choice)
    winOrLose()
    panel.update()
print ("CONGRATS! Your score is")
print (count)
    
# ================ CLEANUP =========================
turtle.mainloop()  # allows for user interactions; handles cleanup



