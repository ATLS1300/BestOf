#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on November 2nd 2021
@author: 
WHAT DOES YOUR GAME DO?
    OBJECTIVE - The user needs to click on the turtle fast enough to get their turtle to the finish line
    RULES - No holding down the click. No cheating!
    CHALLENGE - The user races against speedy turtles to be the first to reach the finish line.
    INTERACTIONS - The enemies move at an automatic speed. The user has to click on the turtle very quickly 
    in order to beat the other turtle track stars!

HOW TO PLAY: After you run the program, use your mouse to hover over and click on the turtle to move forward.
"""
import turtle
import time, random

# ================ LIBRARY SETTINGS SETUP =========================
turtle.colormode(255) # accept 0-255 RGB values
turtle.tracer(0) # turn off turtle's animation

panel = turtle.Screen()
w = 800
h = 800
panel.setup(width=w, height=h)
panel.bgcolor(222, 205, 245) # Thistle

#Borrowed code for the race line and title: https://youtu.be/tXH-cY7N5bg

#Title
turtle.penup()
turtle.goto(-100,350)
turtle.color("black")
turtle.write("Turtle Race!", font = ("Arial",30, "bold")) #Writes title
turtle.hideturtle()

#set up finishline for game
stamp_size = 20
Bsquare_size = 15
Wsquare_size = 15
finish_line = 200

RacelineBlack = turtle.Turtle() #Creating a raceline turtles
RacelineWhite = turtle.Turtle() 

RacelineBlack.color("black")
RacelineBlack.shape('square')
RacelineBlack.shapesize(Bsquare_size / stamp_size)
RacelineBlack.penup()

RacelineWhite.color("white")
RacelineWhite.shape('square')
RacelineWhite.shapesize(Wsquare_size / stamp_size)
RacelineWhite.penup()

#Black squares
for i in range(35): #creates a loop of black squares stamping
    RacelineBlack.goto(finish_line, (400 -(i * Bsquare_size *2)))
    RacelineBlack.stamp()
    
for j in range(35):
    RacelineBlack.goto(finish_line + Bsquare_size, ((400 - Bsquare_size)-(j * Bsquare_size *2)))
    RacelineBlack.stamp()

#white squares
for t in range(35): #creates a loop of white squares stamping
    RacelineWhite.goto(finish_line, (445 -(t * Wsquare_size *2)))
    RacelineWhite.stamp()
    
for k in range(35):
    RacelineWhite.goto(finish_line + Wsquare_size, ((445 - Wsquare_size)-(k * Wsquare_size *2)))
    RacelineWhite.stamp()
    

# ================ VARIABLE DEFINITION & SETUP =========================
running = True

# ================ FUNCTION DEFINITION =========================
# functions should go here IF they work with objects. 
# otherwise, try to include them in classes 

# ================ CLASSES =========================
class UserRacer: 
    def __init__(self,location,racer_color):
        self.color = racer_color
        self.shape = turtle.Turtle(shape='turtle')
        self.shape.shapesize(8)
        self.shape.color(self.color)
        
        self.location = location
        self.shape.up()
        self.shape.goto(self.location)
        
        # onclick functions get called here!
        self.shape.onclick(self.move)
        self.shape.xcor()
        

    def move(self,x,y):
        '''Moves the User forward'''
        global running
        if running:
            self.shape.forward(20)
            self.shape.xcor()
        panel.update()

            
    def checkLocation(self):
        '''If statement for the User to win '''
        global running
        self.shape.xcor()
        if self.shape.xcor() >= 200:
            print("You win!")
            running = False
        panel.update()
            

    # ======== METHODS DEFINITIONS ==========
    # remember: self comes first!

class BotRacers: 
    def __init__(self,location,bot_colors):
        self.color = bot_colors
        self.shape = turtle.Turtle(shape='turtle')
        self.shape.shapesize(8)
        self.shape.color(self.color)
        self.panel = turtle.Screen()
        self.w = 800
        self.h = 800
        self.panel.setup(width=self.w, height=self.h)
            
        #moves turtle to start location
        self.location = location
        self.shape.up()
        self.shape.goto(self.location)
    
    
    def forward(self):
        '''This while loop moves the BotRacers'''
        global running
        time.sleep(0.05)
        self.shape.forward(random.randint(10, 15)) #random speed to add variation in BotRacer speed
        self.shape.xcor()
        panel.update()
        if self.shape.xcor() >= 200:
            print("You lose.")
            running = False

        
panel.listen()
# ================ OBJECTS =========================
userRacer1 = UserRacer((-390,250),(254, 95, 85)) #Orange Red Crayola
botRacer1 = BotRacers((-390,100), (42, 98, 143)) #Lapis Lazuli
botRacer2 = BotRacers((-390, -50), (133, 255, 158)) #Mint Green
botRacer3 = BotRacers((-390,-200), (45, 30, 47)) #Dark Purple

while running: #has the bots moving forward
    for i in range(5):
        botRacer1.forward() 
        botRacer2.forward()
        botRacer3.forward()
        userRacer1.checkLocation()
        panel.update()
    
panel.update()
# ================ CLEANUP =========================
turtle.mainloop()  # allows for user interactions; handles cleanup
