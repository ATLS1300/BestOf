#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 11:30:30 2021
@author: 
Edited by: 
I spoke with her before I edited her code and she said she wanted a green circle in the
background and then sunglasses around his eyes, instead of the singular big blue square
she originally had over one of his eyes
Edit: made square smaller and added another one to make sunglasses 
"""

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen() 
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("OliveDrab")
panel.bgpic(image)

#=======Add your code here==========
circle = turtle.Turtle()  #I created a circle variable for the circle, instead of using turtle.
circle.up()

#features of pen
circle.color("OliveDrab1")
circle.pensize(10)
circle.goto(250,100)

#makes circle 
circle.down()
circle.circle(10) #this will make green circle 
circle.up()


#this will make the blue sunglasses around his eyes 
square1 = turtle.Turtle() #I created square1 variable, instead of turtle.
square1.up()

#features of pen
square1.color("MediumBlue")
square1.pensize(10)

#where first square will start 
square1.goto(-45,130) #I changed the location so it would be more centered around his eyes
square1.down()
square1.left(15) #added this angle of where I want first side in sunglasses to go, more aligned with his eyebrows 

#this loop creates first square in sunglasses
for i in range(4):
    square1.forward(50) #I made the square smaller so it fit his eyes more
    square1.right(90) 
square1.up()
    

#this is for second square of sunglasses that I added to her code 
square2=turtle.Turtle() #I named this variable square2
square2.up()

#pen features 
square2.color("MediumBlue") 
square2.pensize(10)

#where second square will start 
square2.goto(-45,130) #went to same location of first square, then will move forward
square2.left(15) #need to have same angle as first square
square2.forward(60) #moving pen forward to spot where I want loop to start for second square

square2.down() #want to move forward before I put pen down 

for i in range(4):
    square2.forward(50) #kept same size of square, which is smaller than ella's original
    square2.right(90) 

    #turtle.goto(39,5) - commented this out because she didn't need it 

'''Criticism sandwich: The code quality was pretty good before I edited it, 
she only had a couple lines of code that didn't need to be there and it was
a little disorganized, there were like 4 big chunks of code, but overall it 
was good! To improve your code, I think you could delete some of the lines 
that were unnecessary and split up your code more. You could also name your
 different shapes as variables so it is more clear what you're trying to do. 
 And since you wanted it to have squares that looked like sunglasses around 
 his eyes, you could add another for loop for the other square. You could 
 also make the square smaller. I added another for loop for the other 
 square and made them smaller and changed the angle they started out so 
 they'd be more in line with his eyebrows. I also created variable names, 
 explained what the loops would do and split the code up so it looked more 
 organized. I also changed the location of the square so it was closer to his
 eye. I really liked the colors you chose and how you already knew how to do 
 a for loop at this point for a square! I definitely think you have progressed
 a lot and know how to split up code more efficiently and know how to create 
 multiple for loops. I have seen ella's recent work and it is amazing, 
 she has progressed a lot!'''
