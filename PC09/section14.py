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

# ================ VARIABLE DEFINITION & SETUP =========================
import turtle, random
turtle.colormode(255)
turtle.tracer(0)

panel = turtle.Screen()
running = False
starting = True
ending = False
count = 0
choice = .125
# ================ FUNCTION DEFINITION =========================
# functions should go here IF they work with objects. 
# otherwise, try to include them in classes 

# ================ CLASSES =========================
def setup():
    global panel
    w = 700
    h = 800
    panel.setup(width=w, height=h)
    
    background_color = (245, 245, 220)
    panel.bgcolor(background_color)
    
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
        self.shape.goto(random.randint(-350,350), 400)
        self.shape.speed(1)
        count += 1
        panel.update
        
class Introscreen(turtle.Turtle):
    def __init__(self, x, y=0):
        super().__init__()
        self.y = y
        self.x = x
        self.goto(self.x, self.y)
        
        panel.addshape("PRESS START TO BEGIN.gif")
        self.shape("PRESS START TO BEGIN.gif")
        self.up()
        panel.onscreenclick(self.begin)
        
    def begin(self,x,y):
        global running, starting
        self.hideturtle()
        running = True
        panel.update()
        starting = False

class Endscreen(turtle.Turtle):
    def __init__(self, x=100, y=100):
        super().__init__()
        self.y=y
        self.x=x
        self.goto(self.x, self.y)
        
        panel.addshape("GAME OVER.gif")
        self.shape("GAME OVER.gif")
        self.up()

def run():
    def winOfOne():
        global running, ending
        if Button1.shape.ycor() <= -400:
            running = False
            ending = True
        if Button2.shape.ycor() <= -400:
            running = False    
            ending = True
        
    Begin = Introscreen(0)
    Begin.up()
    
    Button1 = Turtles('blue', (-200,300))        
    Button2 = Turtles('green', (200,300))
    
    setup()
    panel.update
    
    while starting:
        panel.update()
    while running:
        Button1.shape.forward(choice)
        Button2.shape.forward(choice)
        winOfOne()
        panel.update()
    
    print ("Congratulations, your score is:")
    print (count)
    
    End = Endscreen(0,0)
    End.up()
    
    panel.update
    while ending:
        panel.update()
    
    turtle.mainloop()

run()



