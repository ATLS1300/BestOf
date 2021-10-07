#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 18:48:42 2021
@author: 
Edited by:
multiple stars drawn in all different colors and sizes around the screen using for loops
edit: made all stars uniform sizes
"""
# import library and set up turtle speed, colormode, and background color

# ------------------------------- set up ----------------------------------
import turtle
turtle.colormode(255)
turtle.bgcolor(0,0,0)


# added section to define lists and variables
# ---------------------------- define lists -------------------------------
loc = [(-100,40),(-120,190),(-90,-250),(100,280),(-305,-160),(290,-160),(205,120),(250,60)] # made list of locations for turtle to go to
colors = ["chartreuse","DeepPink1","violet","yellow","cyan","white","MediumPurple1","blue"] # made list of colors to cycle through



# -------------------- define turtle and variables ------------------------
star = turtle.Turtle()
star.speed(10)
size = 170 # defined variable for the size of each star
degrees = 170 # defined variable for degrees the turtle turns



# consolidated everything by making a nested for loop, running through lists, 
# and defining variables instead of hard coding everything in separate for loops



# ------------------------- perform tasks ------------------------------
for i in range(8): 
    star.color(colors[i])
    star.penup()
    star.goto(loc[i])
    star.pendown()
    
    for iteration in range (0,37):
        star.forward(size)
        star.right(degrees)

""" the code did what it needed to do and was as organzied as it could be
 given the skill level I had at the time. It would have been much easier to 
 make a for loop to have the shapes be drawn repeatedly instead of drawing 
 them all separately. I really liked the use of fun colors and contrast on
 the black background. To be able to now realize how my old code could now be 
 transformed into something much cleaner and much more concise taking up only half
 the amount of lines as the original code is really promising to notice and I 
 think I am making good progress learning the language"""

""" criticism from a friend: figure out how to keep the shapes all the different
 sizes instead of taking the easy way and making them all the same size with a 
 variable. Maybe have a list of sizes and have the size chosen from that list at random"""
