#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on October 29th, 2021.

@author: 

WHAT DOES YOUR GAME DO?
    OBJECTIVE - prevent all the shapes from hitting the right boundary of the screen 
                5 times before clicking them all, turning them from grey to white (grey to 
                accomodate for those who are colorblind)
                (https://chorus.scs.carleton.ca/wp-content/papercite-data/pdf/napoli2018-colourblindgame-chilbw.pdf)
    RULES - use your mouse to click all of the shapes before they hit the right side of the screen the 5th time
    CHALLENGE - the player can only click one shape at a time while the shapes move at a fast pace
    INTERACTIONS - shapes start as grey and once they are clicked they turn white 

"""

import turtle

# ================ LIBRARY SETTINGS SETUP =========================
turtle.colormode(255) # accept 0-255 RGB values
turtle.tracer(0) # turn off turtle's animation

panel = turtle.Screen()
w = 800
h = 800
panel.setup(width=w, height=h)
start_bg = (0,0,0)
panel.bgcolor(start_bg)

# ================ VARIABLE DEFINITION & SETUP =========================
running = True
count = 0
count2 = 0
counter = 1

# ================ CLASSES =========================
class Shapes:
    def __init__(self,loc,color):
        self.shape = turtle.Turtle(shape = "triangle")
        self.shape.shapesize(4)
        self.color = color
        self.shape.color(self.color)
        
        self.location = loc
        self.shape.up()
        self.shape.goto(self.location)
        self.shape.onclick(self.disappear)
        panel.listen()
        panel.update()
        
    # ======== METHODS DEFINITIONS ==========
    def disappear(self,x,y):
        self.shape.color("white")
        global count 
        count += 1
        print(count)
        panel.update()
        
class subClassWin(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("grey")
        self.write("You Win!",move = False,align="center",font=("Arial",30,"bold"))

class subClassLose(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("grey")
        self.write("You Lose :(",move = False,align="center",font=("Arial",30,"bold"))

# ================ OBJECTS =========================
# from top to bottom 1 - 6
grey1 = Shapes((-400,286),"grey")
grey2 = Shapes((-400,172),"grey")
grey3 = Shapes((-400,58),"grey")
grey4 = Shapes((-400,-56),"grey")
grey5 = Shapes((-400,-170),"grey")
grey6 = Shapes((-400,-284),"grey")

# ================ ANIMATION LOOP =========================
while running:
    for i in range(counter):
      grey1.shape.forward(1)
      xpos = grey1.shape.xcor()
      grey2.shape.forward(1)
      grey3.shape.forward(1)
      grey4.shape.forward(1)
      grey5.shape.forward(1)
      grey6.shape.forward(1)
     
      if count >= 6:
          running = False
          subClassWin()
          print("you win")
      if xpos <= -415 or xpos >= 415: 
          grey1.shape.right(180)
          grey2.shape.right(180)
          grey3.shape.right(180)
          grey4.shape.right(180)
          grey5.shape.right(180)
          grey6.shape.right(180)
          print("you're gonna lose")
          count2 += 1
          
      if count2 >= 5:
          running = False
          subClassLose()
          print("you lose")

    panel.update() # update the window with everything drawn in a single frame
    
# ================ CLEANUP =========================
turtle.mainloop()  # allows for user interactions; handles cleanup



