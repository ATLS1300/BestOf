#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 11/02/2021

@author: 

WHAT DOES YOUR GAME DO?
    OBJECTIVE - See how many cookies Santa Clause can eat before the kid
                comes out to open presents!
    RULES - The user can click their mouse to move Santa from left to right 
            to catch/eat the cookies. 
    CHALLENGE - Eating/catching the cookies count if they are caught in the relm
                of Santa Clause's head. 
    INTERACTIONS - As the player moves Santa Clause across the screen to 
                    catch/eat the cookies, the user's score will be kept.
                    After 30 seconds you will either win or lose the game.
                    The kid will come out with 5 seconds left, as a sign the 
                    game is almost over. The cookies will also slow down with
                    5 seconds left.
"""
import turtle
import time, random

# ================ LIBRARY SETTINGS SETUP =========================
turtle.colormode(255) # accept 0-255 RGB values
turtle.tracer(0) # turn off turtle's animation

panel = turtle.Screen()
w = 800
h = 800

# import and set santa as turtle
santa = turtle.Turtle()

# ================ VARIABLE DEFINITION & SETUP =========================
running = True
cookie_count = 0
cookietop_count = 0

rules = turtle.Turtle()

#writing the rules on the screen
rules.hideturtle()
rules.up()
rules.goto(-375,350)
rules.write("If Santa can catch 25 cookies in 30 seconds, he wins!!",move = True,font = ("Courier", 22, "normal"))

rules.goto(-350,320)
rules.write("A kid will appear when there are 5 seconds left",move = True,font = ("Courier", 22, "normal"))

rules.goto(-350,290)
rules.write("& the cookies will slow down...",move = True,font = ("Courier", 22, "normal"))


# ================ FUNCTION DEFINITION =========================
# functions should go here IF they work with objects. 
# otherwise, try to include them in classes 
def move_santa (x,y):
    """when screen clicked, santa moves"""
    santa.setx(x)
    santa.speed(10)
    
    
def setup():
    panel.setup(width=w, height=h)
    santaImg = "santa.gif" 
    panel.addshape(santaImg) # save the gif to the panel so it knows what to draw
    santa.shape(santaImg) # change the turtle shape to ghost gif
    santa.up()
    santa.sety(-200) # making the turtle start lower up on the screen

    #set up images for game
    panel.bgpic("backgroundpic.gif")
    panel.bgcolor("peachpuff4")
    
    panel.onscreenclick(move_santa) #call back function
    
setup()
# ================ CLASSES =========================
class Kid(turtle.Turtle): # using turtle in class
    def __init__(self):
        super().__init__()
        self.RenameThisAttribute = []
        kidImg = "kid.gif" 
        panel.addshape(kidImg) # save the gif to the panel so it knows what to draw
        self.shape(kidImg) # change the turtle shape to cookie gif
        self.up()
        self.sety(0) # making the kid start middle of screen
        self.setx(-440) #make kid go off the screen
        
    def walkin(self): #make kid walk onto screen. sign that game is almost over
        if self.xcor() == -440:
            for i in range (10):
                self.forward(10)
                panel.update() 
                
class Cookie(turtle.Turtle): # using turtle in class
    def __init__(self):
        super().__init__()
        self.RenameThisAttribute = []
        cookieImg = "cookie.gif" 
        panel.addshape(cookieImg) # save the gif to the panel so it knows what to draw
        self.shape(cookieImg) # change the turtle shape to cookie gif
        self.up()
        self.sety(h/2) # making the turtle start higher up on the screen
        # onclick functions get called here
        
    def cookie_fall(self, santa_xpos, cookiespeed): #3 parameters
        global cookie_count
        global cookietop_count
        y = self.ycor()
        x = self.xcor()
        if y < -300: # if statement for when cookie touches bottom of screen
            y = h/2 - random.randint(1,100)
            r = random.randint(-400,400)
            self.setx(r)
            cookietop_count = cookietop_count + 1
        if y > -300 and y < -50 and abs(x - santa_xpos) < 100: # if statement that keeps score
            y = h/2 - random.randint(1,100)
            r = random.randint(-400,400)
            self.setx(r)
            cookie_count = cookie_count + 1
            cookietop_count = cookietop_count + 1 
            print(cookie_count)
        self.sety(y-cookiespeed)
    
# ================ OBJECTS =========================
# instantiate objects here
cookielist = []
for i in range(5):
    cookielist.append(Cookie())
    
kid = Kid()

# ================ ANIMATION LOOP =========================
# PRO-MOVES - can you get this while loop into a class? 
# You will have to for PC09.
turtle.hideturtle()
turtle.up()
turtle.goto(-330,97)


while running:
    santa_xpos = santa.xcor() 
    cookiespeed = 15
    if cookietop_count > 25: # kid walksin, game over soon
        kid.walkin()
        cookiespeed = 5
        
    if cookietop_count > 30: # game over
        running = False #stops the while loop after 10 times
        print("score:") # string shows the score
        print(cookie_count) # shoes score in terminator
        if cookie_count > 25:
            turtle.write("You Win!!",move=True,font=("Courier",25,"normal"))
            
        else:
            turtle.write("You Lose:(",move=True,font=("Courier",25,"normal")) 
            
    for cookie in cookielist:
        cookie.cookie_fall(santa_xpos, cookiespeed)  
    panel.update() # update the window with everything drawn in a single frame
    
# ================ CLEANUP =========================
turtle.mainloop()  # allows for user interactions; handles cleanup

'''Very nice, I love how festive it is, but I couldnt get 25 cookies (said by friend, XX, after playing our game)''' 


