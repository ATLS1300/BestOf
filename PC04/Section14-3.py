# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 16:32:07 2021

"""

# a eye with randomly selected iris color, and a pupil that changes colors from a randomly selected palette
# this eye is framed by a parametric heart

import math, turtle, random

# create panel
panel = turtle.Screen()
w = 600
h = 600
panel.setup(width = w, height = h)

turtle.colormode(255) # import RGB colors

# set background color
panel.bgcolor(0,0,0)

#change pen color
turtle.pencolor(83, 97, 96)
# creating parametric heart - referenced from https://canvas.colorado.edu/courses/75648/pages/parametric-patterns

scale = 3 # to scale up the pattern so it's visible

ANGLES = range(0,1800)

for angle in ANGLES:
    
    angle = math.radians(angle)/10 # change division value to increase "smoothness" of lines

    X = 300*(1/6*math.sin(2*angle)*(1 + math.cos(80*angle))*(1-1/12*(math.sin(2*angle))**8))

    Y = 300*(-1/2*(2*angle/math.pi - 1)**2 + 1/7*math.sin(2*angle)*(math.sin(80*angle)**3))

    X*=scale # make the image larger so it's visible

    Y*=scale
    
    turtle.goto(X,Y+200) # make turtle follow the equation, add to x or y to change the position of turtle


# palettes, generated from coolors.co 
peachyBlue = ( (48,53,102), (73, 106, 129), (102, 153, 155), (179, 175, 143), (255, 196, 130) ) 
pastelPinkBlue = ((157, 133, 141), (187, 160, 178), (164, 168, 209), (164, 191, 235), (140, 171, 190))
seaGreens = ((188, 182, 255), (184, 225, 255), (169, 255, 247), (148, 251, 171), (130, 171, 161))
reddishBrowns = ((204, 201, 161), (240, 255, 206), (165, 63, 43), (76, 35, 10), (40, 0, 4))
saturatedColors = ((0, 39, 43),(224, 255, 79), (255, 102, 99),(255, 46, 204),(165, 16, 128))
darkerPurples = ((242, 215, 238),(211, 188, 192),(165, 102, 139),(105, 48, 109),(14, 16, 61))

# list of palettes
eyePalettes = [peachyBlue, pastelPinkBlue, seaGreens, reddishBrowns, saturatedColors, darkerPurples]

randomEyePalettes = random.choice(eyePalettes) # selects a random eye color palette when used

schleraColor = (255,255,255) # color for the schlera

turtle.pencolor(255,255,255)

outerEye = turtle.Turtle()

# making the outer eye
outerEye.fillcolor(schleraColor)
outerEye.begin_fill()
outerEye.up()
outerEye.goto(-150,0)
outerEye.down()
outerEye.right(45)
outerEye.circle(200,90)
outerEye.left(90)
outerEye.circle(200,90)
outerEye.end_fill()

iris = turtle.Turtle()

# making the iris
irisColor = random.choice(randomEyePalettes) # selects a random palette then a random color from that palette
iris.fillcolor(irisColor)
iris.begin_fill()
iris.up()
iris.goto(0,-50)
iris.setheading(0)
iris.down()
iris.circle(55)
iris.end_fill()

turtle.up()
turtle.goto(0,-20)
turtle.down()

#making the pupil and cycling it through the colors of a randomly selected palette
for colors in randomEyePalettes: 
    turtle.setheading(0)
    turtle.fillcolor(colors)
    turtle.begin_fill()
    turtle.circle(23)
    turtle.end_fill()
    
turtle.done()

    