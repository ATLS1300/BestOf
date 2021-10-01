#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 18:19:40 2021
Ugly spaghetti art :)

"""

import turtle, random
turtle.speed(10)
panel = turtle.Screen().bgcolor('white')
littleArt = turtle.Turtle()
palette = ["MidnightBlue", "DarkRed", "OrangeRed", "LightYellow"]


littleArt.goto(random.randint(100,300),random.randint(100,300))
size = 1

# modified from for loop warm up
for i in range(4):
    littleArt.color(palette[i])
    littleArt.width(size)
    size += 1

    littleArt.circle(random.randint(10,41))
    littleArt.forward(random.randint(1,26))

moreLittleart = turtle.Turtle()

inc = 3
numIt = 100

randomCol = ['red', 'pink', 'orange', 'yellow', 'green', 'blue', 'purple']

moreLittleart.goto(random.randint(100,300),random.randint(100,300))

for i in range(numIt):
    moreLittleart.color(random.choice(randomCol)) # randomizing color choice
    moreLittleart.goto(random.randint(100,300),random.randint(100,300)) # randomizing placement

    for i in range(inc):
      moreLittleart.width(random.randint(1, 11)) # randomizing thickness
      moreLittleart.down()
      moreLittleart.shape("triangle")
      moreLittleart.forward(150)
      moreLittleart.left(120)
    
    moreLittleart.right(100)
    
turtle.done()