#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 21:22:34 2021

@author: rachelwildeson
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on October 16, 2021


DEAR USER, 
    The object of the game is to click the ghost that drifts into view in the screen.
    If you are able to *click* the ghost in time before it disappears behind the red square, You Win!
    To play the game, click the green arrow in the top menu box of the screen. A popup window will appear with the game. 

- This code sends an image of a ghost back and forth along the screen. The ghost pops out from behind the red screen back into the left panel.
- I showed this code to my partner and he said I have some good building blocks to make a more exciting and interactive game. He also commented that my code provided a solid framework to build upon. He also said that the content of my interaction was very on theme for October. 
- Target Audience: I tried to make this accessible to my parents to interact with. Both of my parents have pretty poor eyesight and are both farsighted. Neither of them interact much with technology or games for that matter. In researching for ideas on how to make this more accessible to them, I found that high contrast is key and that products geared to be accessible to older people should not use the color blue as it makes things more difficult to differentiate on the screen. I also included some text that reads what you are suppose to do for the 'game' so directions are clear and visible with how you run the script and what to do!    

"""

import turtle

# ================ LIBRARY SETTINGS SETUP =========================
turtle.colormode(255) # accept 0-255 RGB values
#turtle.tracer(0) # turn off turtle's animation

panel = turtle.Screen()
w = 700
h = 500
panel.setup(width=w, height=h)
panel.bgcolor("black")

# ================ VARIABLE DEFINITION & SETUP =========================
#define turtle objects, variables, etc. here!
running = True
x = 300

ghostSmallOne = turtle.Turtle(shape="circle")
ghostImgSmallOne = "ghostsmallone.gif" 
panel.addshape(ghostImgSmallOne) 
ghostSmallOne.shape(ghostImgSmallOne) 

ghosts = [ghostSmallOne]
# ================ FUNCTION DEFINITION =========================
# define your functions here! Use descriptive names and don't forget 
# a docstring!

def ghostPath(turt, leftAngle=10, distance =500, rightAngle=195):
    ''' Sends ghost diagnally along screen and the path goes back and forth '''    
    for i in range (2):
      turt.left(leftAngle)
      turt.forward(distance)
      turt.right(rightAngle)
      turt.forward(distance)
      for i in range (1):
          turt.left(-leftAngle)
          turt.forward(-distance)
          turt.right(-rightAngle)
          turt.forward(-distance)

def youWin (x,y):
    '''Prints You Win in the Command Line '''   
    print("You Win!")
        
# ================ ANIMATION LOOP =========================
   
square = turtle.Turtle(shape='square')
square.hideturtle()
square.goto(300,0)
square.showturtle()
square.down()
square.color('red')
square.shapesize(30)

ghosts[0].hideturtle()
ghosts[0].up()
ghosts[0].goto(-275,-50)
ghosts[0].showturtle()

ghosts[0].onclick(youWin)
while running:
  ghostPath(ghosts[0])
  

    # call functions and conditional statement to stop loop (if desired) 
      
    #panel.update() # update the window with everything drawn in a single frame
    
# ================ CLEANUP =========================
turtle.mainloop()  # allows for user interactions; handles cleanup