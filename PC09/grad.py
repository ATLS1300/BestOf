#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 10/31/21


This is a matching game that allows the player to click through
4 different turtles to increase their score.

    OBJECTIVE - Try not to color match the top right turtle.
    
    RULES - Get as high of a click count as possible before
            you get matched
            
    CHALLENGE- The top left turtle holds the "match color".
               The other 4 turtles will change color as you
               click them, but player doesn't know when these
               4 will get to the "match color" because they
               change color randomly. Increase your chances
               of getting a high score by alternating clicks
               between the 4 turtles (instead of clicking just one)
               
    INTERACTIONS - Click the turtles at the top right, middle,
                   bottom left, and bottom right to change the
                   colors of the turtles randomly each click.
"""

import turtle, random
import time

# ================ CLASSES =========================
class ClickButton():
    
    def __init__(self, buttoncolor, x=0,y=0):      
        #button shape and size
        self.shape = turtle.Turtle(shape='turtle')
        self.shape.shapesize(5,5,5) # increase turtle size
   
        
        # set up button color
        self.color = buttoncolor
        self.shape.color(self.color)
       
        # set a location for the button 
        self.x = x
        self.y = y
        self.shape.up()
        self.shape.goto(self.x,self.y)
        
        #interactivity
        self.shape.onclick(self.doEverything)
       
        panel.update() # update panel
    
     # ======== METHODS DEFINITIONS ==========
    # remember: self comes first!
    def changer(self):
        '''change turtle shape color randomly when clicked,
        add each click color to end of rainbow color list'''

        choice = random.choice(rainbow)
         
        self.shape.color(choice)
        rainbow.append(choice)

    def countMe(self):
        ''' counter that counts each button press and outputs
        # clicks to console. Also outputs when game is over
        and final score. '''
        
        global counter
        string1 = "Game Over. Final Score:"
        string2 = " clicks."
              
        if running==True: #add 1 to counter if true
            counter+=1
            print(counter,string2,rainbow[-1])
        else: 
            print(string1, counter, string2)
            
    def box(self):
        ''' Draw a box around the static color turtle and
        write some instruction text '''
        
        #box setup
        outline = turtle.Turtle(visible=False)
        outline.up()
        outline.goto(-275,130)
        
        #instruction text
        instructions = turtle.Turtle(visible=False)
        instructions.up()
        instructions.goto(-275, 115)
        instructions.write("Try not to match my color! I am " + turtchoice + ". Click me for your score.")
        
        for i in range(2):
            outline.down()
            outline.forward(200)
            outline.left(90)
            outline.forward(145)
            outline.left(90)   
       
    def doEverything(self,x,y):
        ''' Do everything in the included methods (on click) '''

        self.changer()
        self.countMe()
        self.box()
           
#second class to output score
class Write(ClickButton):
    
    def __init__(self, buttoncolor, buttontext, x=-200,y=200):
        super().__init__(buttoncolor,x,y)        #inherit buttoncolor,x,y,attributes from ClickButton
       
        #button text  
        self.text = buttontext
    
        #interactivity
        self.shape.onclick(self.doNothing)
       
        panel.update() # update panel

    # ======== METHODS DEFINITIONS ==========
    # remember: self comes first!
        
    def countScore(self):
        ''' writes score by the example turtle '''
        score = turtle.Turtle(visible=False)
        count = turtle.Turtle(visible=False)
      
        score.up()
        count.up()

        score.setposition(-100,200)
        count.setposition(-90,190)
        
    
        score.write(self.text, align='left')
        
        count.write(counter)
        time.sleep(1)
        
        count.undo()
    def gameOver(self):
        '''Writes game over'''
        gameover = turtle.Turtle(visible=False)
        gameover.up()
        gameover.setposition(0,150)
        
        
        if running == False:
            gameover.write ("Game Over")
            
    def doNothing(self,x,y):
        '''Does everything in the included methods (onclick)'''
        self.shape.color(turtchoice) # don't change color on click
        self.countScore() #count the score
              

# ================ FUNCTION DEFINITION =========================
# PRO-MOVES - can you get this while loop into a class? 
# You will have to for PC09.
class Game():
    
    def __init__(self):
        
        # start the game
        self.setup()

    def setup(self):
        '''Creates screen, background and start conditions for
        game'''
        global panel
    
        turtle.colormode(255) # accept 0-255 RGB values
        turtle.tracer(0) # turn off turtle's animation

        panel = turtle.Screen()
        w = 600
        h = 600
        panel.setup(width=w, height=h)

        # set panel color
        bgcolor = (220, 253, 216) # light green
        panel.bgcolor(bgcolor) #set panel color
    
        self.run()  
    

    def run(self):
        '''Houses variables and runs the code to execute the game.
        '''
        # what variables need to be seen everywhere?
        global running, rainbow, turtchoice, counter
    
        #define variables
        rainbow = ["violet","blue","pink","green", "yellow", "red","orange"] #list of colors
        turtchoice = random.choice(rainbow) #color to match
        running = True
        counter = 0 #score
        endColor = 'black'
    
        # instantiate objects
        topRight = ClickButton("lavender",200,200)
        bottomLeft = ClickButton("skyblue3",-200,-200)
        bottomRight = ClickButton("bisque", 200,-200)
        middle = ClickButton("chartreuse")
        topLeft = Write(turtchoice,"Score: ")

    
        # ================ ANIMATION LOOP =========================
        while running:
        
            if rainbow[-1] == turtchoice: 
                running = False
                
                time.sleep(3)
                topLeft.shape.color(endColor) #turn match/example turtle black
                rainbow.append(endColor) #add black to the end of rainbow
                topLeft.gameOver() #print game over on screen
  
            panel.update() # update the window with everything drawn in a single frame
     
        # ================ CLEANUP =========================
        turtle.mainloop()  # allows for user interactions; handles cleanup

# ================== SETUP & ANIMATION =====================
if __name__=='__main__':
    Game()
    
    


'''
Feedback from friend/player: Super cool game, I liked how there was an example turtle and
                             we could pick between any of the others to increase my score.        
                             I wish the scoreboard was always showing, like the number of
                             clicks I've done. Having to check my score was a bit difficult.
                             I really liked how I could see how many counts total though in
                             the box on the other screen. Maybe it would have been cooler
                             if the turtles moved around a little bit? Like the ones you
                             were supposed to click. It would be more challenging probably,
                             or maybe if there were more than 4 turtles that changed color.                             
'''