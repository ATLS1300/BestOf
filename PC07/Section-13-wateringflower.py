#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Oct. 15, 2021

@author: Section 13 anon

Simple game where the user controls a raining cloud (clicks to move it)
and tries to water flowers. After letting 3 raindrops hit the flower, it is happy
and needs no more water.
"""

import turtle

# ================ LIBRARY SETTINGS SETUP =========================
turtle.colormode(255) # accept 0-255 RGB values

panel = turtle.Screen()
w = 700
h = 500
panel.setup(width=w, height=h)
panel.bgcolor("sky blue")

# ================ VARIABLE DEFINITION & SETUP =========================
#define turtle objects, variables, etc. here!

# create raindrop turtles
raindrop1 = turtle.Turtle()
raindrop1.up()
raindrop1.goto(0,200)
raindrop1.right(90)
raindrop1.hideturtle()

raindrop2 = turtle.Turtle()
raindrop2.up()
raindrop2.goto(0,200)
raindrop2.right(90)
raindrop2.hideturtle()

raindrop3 = turtle.Turtle()
raindrop3.up()
raindrop3.goto(0,200)
raindrop3.right(90)
raindrop3.hideturtle()

# put the raindrop turtles into a list

drops = [raindrop1, raindrop2, raindrop3]

# adhere raindrop image to the raindrop turtles
rainImage = "raindrop.gif"
panel.addshape(rainImage)

raindrop1.shape(rainImage)
raindrop2.shape(rainImage)
raindrop3.shape(rainImage)

# create cloud turtle

cloud = turtle.Turtle()
cloud.up()
cloud.goto(0,200)

# adhere cloud image to cloud turtle
cloudImage = "cloud.gif"
panel.addshape(cloudImage)

cloud.shape(cloudImage)

# create flower turtle
flower = turtle.Turtle()
flower.up()
flower.goto(200,-150)

# import all of the flower images
sadFlower = "sadflower.gif"
panel.addshape(sadFlower)

happyFlower = "happyflower.gif"
panel.addshape(happyFlower)

onedropFlower = "1drop.gif"
panel.addshape(onedropFlower)

twodropFlower = "2drop.gif"
panel.addshape(twodropFlower)

# have flower start as sad (no water)
flower.shape(sadFlower)

waterCount = 0 # keep track of how many raindrops hit the flower

running = True

# ================ FUNCTION DEFINITION =========================
# define your functions here! Use descriptive names and don't forget 
# a docstring!
    
def wateringFlowers(speed=3):
    global waterCount
    for i in range(len(drops)):
        drops[i].speed(speed)
        if drops[i].xcor() == cloud.xcor() and drops[i].ycor() == cloud.ycor(): # make sure that raindrop is directly behind cloud
            drops[i].showturtle()
            drops[i].goto(cloud.xcor(), -250) # raindrop fall down from cloud
            if 150 < drops[i].xcor() < 240: # if raindrop comes close to flower
                waterCount += 1 # the raindrop has hit the flower
            drops[i].hideturtle()
            # change flower image based on how many water drops hit
            if waterCount == 1: 
                flower.shape(onedropFlower)
            elif waterCount == 2:
                flower.shape(twodropFlower)  
            elif waterCount == 3:
                flower.shape(happyFlower)
                turtle.hideturtle()
                turtle.up()
                turtle.goto(-120,-160)
                turtle.write("Thank you!", font=("Helvetica",
                                40, "normal"))
                turtle.done()                    
                
        else: # if the raindrop isn't behind the cloud, move it there
            drops[i].speed(0)
            drops[i].goto(cloud.xcor(),cloud.ycor())
            drops[i].speed(speed)
    
    for i in range(3): # if rain falls off screen, move it back to cloud
        if drops[i].ycor() <= -250:
            drops[i].speed(0)
            drops[i].goto(cloud.xcor(),cloud.ycor())
            drops[i].speed(speed)
# ================ ANIMATION LOOP =========================
while running:
    panel.onclick(cloud.goto) # click on screen to move cloud
    wateringFlowers()
      
    panel.update() # update the window with everything drawn in a single frame
    
# ================ CLEANUP =========================
turtle.done()



