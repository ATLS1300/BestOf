"""
Created on Thu Sep 15 11:39:56 2020
PC04 Gen Art
@author: 

The first turtle creates a warm color spiral that overlaps itself and fills up 
the screen. Then the second turtle creates a cool color archamedian spiral that 
is on top of the warm spiral to emphasize the contrast in colors. The art piece 
can be a symbol of the varying emotions we have as humans that range from hapiness 
(warm colors) to sadness (cool colors) and how often in life we have to find a way 
to balance these emotions.

"""
import turtle
import math, random

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 700 # width of panel
h = 700 # height of panel
panel.setup(width=w, height=h) 

# =============== ADD YOUR CODE BELOW! =================
panel.bgcolor(0,0,0) #set background color to Black

WarmSpiral = turtle.Turtle() #create turtle named WarmSpiral
WarmSpiral.pensize(2) #set WarmSpiral wifth to 2
WarmSpiral.speed(10) #set WarmSpiral pen speed to the max (10)

WarmColors = ["#F0544F", "#FF7F11", "#FF1B1C"] #create a list of HEX values

#modified from https://www.youtube.com/watch?v=0Pe4BHTaQCk
for x in range(450): #for loop that creates overlapping spiral with 450 iterations
    WarmSpiral.color(random.choice(WarmColors)) #used random.choice to randoly select a color from the WarmColors list
    WarmSpiral.width(x/100+1) #the width of the WarmSpiral pen increases with each iteration
    WarmSpiral.forward(x)
    WarmSpiral.left(66) #the angle increment between each figure drawn is 66 degrees
    
CoolSpiral = turtle.Turtle() #create turtle named CoolSpiral
CoolSpiral.pensize(3)
CoolSpiral.speed(10)

CoolColors = ["#480ca8", "#4361ee", "#4cc9f0"] 

for i in range(600): #for loop that creates an archemedian spiral utilizing math functions pi, sin, & cos
    CoolSpiral.color(random.choice(CoolColors)) #used random.choice to randomly select a color from the CoolColors list
    vt = i / 40 * math.pi
    y = (vt * 8) * math.sin(vt)
    x = (vt * 8) * math.cos(vt)
    CoolSpiral.goto(x,y)

# =================== CLEAN UP =========================
turtle.done()
