#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Nov. 4th 2021
@author: Netta Ofer

WHAT DOES YOUR GAME DO?
    OBJECTIVE - Populate the triangles by clicking on them
    RULES - the user can click on the triangles
    CHALLENGE - Populate the triangles as much and fast as possible
    INTERACTIONS - click the triangles
"""

import turtle
import random

# ================ LIBRARY SETTINGS SETUP =========================
turtle.colormode(255)
turtle.tracer(0)

panel = turtle.Screen()
w = 800
h = 800
panel.setup(width=w, height=h)


# ================ VARIABLE DEFINITION & SETUP =========================
running = True
COLORS = ["aquamarine","pink","orange","yellow"]
instanceList = [] 

# ================ CLASSES =========================
# modified from class code
class Triangles(turtle.Turtle):
    def __init__(self, x, y=0):
        super().__init__()
        self.x = x
        self.y = y
        self.shape('triangle')
        self.up()
        self.shapesize(3)
        self.color(random.choice(COLORS))
        self.goto(self.x, self.y)
        
        # onclick functions get called here!
        # self.onclick(self.gotMe)
        self.onclick(self.multiply)
        
# ======== METHODS DEFINITIONS ==========
    # modified from class code:
    def walk(self):
        self.forward(random.randint(3,20))
        self.seth(random.randint(0,360))
        panel.update()
        

    def multiply(self, x,y):
        global instanceList
        X = random.randint(-350,350)
        instanceList.append(Triangles(X))
        print("GO!")
        
# ================ OBJECTS =========================
for i in range(5):
    X = random.randint(-350,350)
    instanceList.append(Triangles(X))
    

# ================ ANIMATION LOOP =========================

while running:
    
    for inst in instanceList:
        inst.walk()
    
    panel.update()
    
    
# ================ CLEANUP =========================
turtle.mainloop()