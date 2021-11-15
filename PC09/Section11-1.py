#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on October 29th, 2021.

@author:

WHAT DOES YOUR GAME DO?
    OBJECTIVE - prevent all the shapes from hitting the left boundary of the screen
                2 times before clicking them all, turning them from grey to white (grey to 
                accomodate for those who are colorblind)
                (https://chorus.scs.carleton.ca/wp-content/papercite-data/pdf/napoli2018-colourblindgame-chilbw.pdf)
    RULES - use your mouse to click all of the shapes before they hit the left side of the screen the 2nd time
    CHALLENGE - the player can only click one shape at a time while the shapes move at a fast pace
    INTERACTIONS - shapes start as grey and once they are clicked they turn white 
    FEATURES - start button, exit button(uper right hand corner), restart button(automatically prompts the user when the game ends)
"""

import turtle, time 

# ================ LIBRARY SETTINGS SETUP =========================

def setup():
    global count, count2, counter, panel
    turtle.tracer(0)
    turtle.begin_poly()
    turtle.right(45)
    for i in range(4):
        turtle.down()
        turtle.goto(0,0)
        turtle.right(90)
        turtle.forward(1)
        turtle.up()
    turtle.end_poly()
    exitsign = turtle.get_poly()
    turtle.register_shape('exit',exitsign)
    

    turtle.colormode(255) # accept 0-255 RGB values
    turtle.tracer(0) # turn off turtle's animation
    
    panel = turtle.Screen()
    w = 800
    h = 800
    panel.setup(width=w, height=h)
    start_bg = (0,0,0)
    panel.bgcolor(start_bg)
    
    ExitButton()
    
    # ================ VARIABLE DEFINITION & SETUP =========================
    count = 0
    count2 = 0
    counter = 1    
# ================ CLASSES =========================

class Shapes(turtle.Turtle):
    def __init__(self,loc,color):
        super().__init__()
        self.shape("triangle")
        self.shapesize(4)
        self.color(color)
    
        self.location = loc
        self.up()
        self.goto(self.location)
        self.onclick(self.disappear)
        panel.listen()
        panel.update()
        
    # ======== METHODS DEFINITIONS ==========
    def disappear(self,x,y):
        self.color("white")
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
        panel.update
        time.sleep(3)
        panel.clear()
              

class subClassLose(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("grey")
        self.write("You Lose :(",move = False,align="center",font=("Arial",30,"bold"))
        panel.update
        time.sleep(3)
        panel.clear()
        
class ExitButton(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("exit")
        self.shapesize(15)
        self.color("grey")
    
        self.up()
        self.goto(350,362)
        self.onclick(self.quitgame)
        panel.listen()
        panel.update()
        
    # ======== METHODS DEFINITIONS ==========
    def quitgame(self,x,y):
        panel.bye()
 
def Run():
    global running, instanceList, count, count2
    instanceList = []
    coordList = [(-400,286),(-400,172),(-400,58),(-400,-56),(-400,-170),(-400,-284)]
    for i in range(6):
        instanceList.append(Shapes(coordList[i],"grey"))
    running = True
    
    panel.onclick(None) # only click once
    while running:
        for i in range(len(instanceList)):
                instanceList[i].forward(1)
         
        if count >= 6:
               running = False
               count2 = 0
               count = 0 
               time.sleep(.05)
               subClassWin()
               print("you win")
               restart()
              
               
        for i in range(len(instanceList)):
              xpos = instanceList[0].xcor()
              
              if xpos <= -415: 
                  instanceList[i].right(180)
                  print("you're gonna lose")
                  count2 += 1
                  print(count2)
                 
              if xpos >= 415:
                  instanceList[i].right(180)
                  count2 += 1
                  print(count2)

        if count2 >= 24:
               running = False
               count2 = 0  
               count = 0
               time.sleep(.05)
               subClassLose()
               print("you lose") 
               restart()

        panel.update()
        
    turtle.mainloop()    
 
class start(turtle.Turtle):
    def __init__(self):
        super().__init__()
        setup()
        self.hideturtle()
        self.color("grey")
        self.write("click anywhere to start",move = False,align="center",font=("Arial",30,"bold"))
        self.goto(0,-50)
        self.write("click all of the shapes before its too late!",move = False,align="center",font=("Arial",20,"normal"))
        panel.onclick(self.StartNow)
        
        turtle.mainloop()
        #======= Methods =========
    def StartNow(self,x,y):
        global running 
        self.clear()
        panel.update()
        Run()
        
class restart(turtle.Turtle):
    def __init__(self):
        super().__init__()
        global panel
        panel.clear()
        setup()
        self.hideturtle()
        self.color("grey")
        self.write("click anywhere to restart",move = False,align="center",font=("Arial",30,"bold"))
        self.goto(0,-50)
        self.write("click all of the shapes before its too late!",move = False,align="center",font=("Arial",20,"normal"))
        panel.onclick(self.StartNow)
        
        turtle.mainloop()
        #======= Methods =========
    def StartNow(self,x,y):
        global running 
        self.clear()
        panel.update()
        Run()
    
          
# ================ ANIMATION LOOP =========================
start()

'''good start with the click to start but maybe try making different levels 
where difficulty increases somehow whether speed of the shapes
increase or more shapes appear etc.'''
