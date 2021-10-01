# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 14:46:17 2021


This code generates 4 trees of coral with random pathing through the window.
Each tree has 2 branches that split off as the tree gets larger. The colors 
for each tree is random, but setup in a way that the branches hold the same
colors as the tree. 

"""

import random
import turtle 
turtle.colormode(255)

panel = turtle.Screen()
w=800
h=600
panel.setup(width=w,height=h)
panel.bgcolor("lightsteelblue1")

#plant starting locations are set below
plantStartPoints=((-240,-300),(-80,-300),(80,-300),(240,-300))

#These are going to be the clones that start drawing the coral
t1=turtle.Turtle()  #Left most tree; Main stalk.
t1b=turtle.Turtle() #Leftmost tree; First branch.
t1c=turtle.Turtle() #Leftmost tree; Second branch.

t2=turtle.Turtle()  #Left-middle tree main stalk.
t2b=turtle.Turtle() #Left-middle; First branch.
t2c=turtle.Turtle() #Left-middle; Second branch.

t3=turtle.Turtle()  #Right-middle tree main stalk.
t3b=turtle.Turtle() #Right-middle; First branch.
t3c=turtle.Turtle() #Right-middle; Second branch.

t4=turtle.Turtle()  #Rightmost tree main stalk.
t4b=turtle.Turtle() #Rightmost tree; First branch.
t4c=turtle.Turtle() #Rightmost tree; Second branch.

#The abomination that is changing initial turtle attributes.
t1.hideturtle()
t1b.hideturtle()
t1c.hideturtle()
t2.hideturtle()
t2b.hideturtle()
t2c.hideturtle()
t3.hideturtle()
t3b.hideturtle()
t3c.hideturtle()
t4.hideturtle()
t4b.hideturtle()
t4c.hideturtle()

t1.penup()
t1b.penup()
t1c.penup()
t2.penup()
t2b.penup()
t2c.penup()
t3.penup()
t3b.penup()
t3c.penup()
t4.penup()
t4b.penup()
t4c.penup()

#Lets setup the colors for each of the coral plants
#These variables will be used in different orders for each plant
A=random.randint(0,255)
B=random.randint(0,255)
C=random.randint(0,255)
D=random.randint(0,255)
E=random.randint(0,255)

t1.goto(plantStartPoints[0])
t2.goto(plantStartPoints[1])
t3.goto(plantStartPoints[2])
t4.goto(plantStartPoints[3])

t1.left(90)
t2.left(90)
t3.left(90)
t4.left(90)

t1.pendown()
t2.pendown()
t3.pendown()
t4.pendown()

t1.pensize(24)
t1b.pensize(24)
t1c.pensize(24)
t2.pensize(24)
t2b.pensize(24)
t2c.pensize(24)
t3.pensize(24)
t3b.pensize(24)
t3c.pensize(24)
t4.pensize(24)
t4b.pensize(24)
t4c.pensize(24)

#Assiging the colors for each of the trees.
#branches hold the same color as the stalk, but they all should be different.
t1.pencolor(A,B,C)
t1b.pencolor(A,B,C)
t1c.pencolor(A,B,C)
t2.pencolor(E,D,C)
t2b.pencolor(E,D,C)
t2c.pencolor(E,D,C)
t3.pencolor(A,D,E)
t3b.pencolor(A,D,E)
t3c.pencolor(A,D,E)
t4.pencolor(B,E,A)
t4b.pencolor(B,E,A)
t4c.pencolor(B,E,A)

t1c.speed(100)
t2c.speed(100)
t3c.speed(100)
t4c.speed(100)

branchPos = [[0,0],[0,0],[0,0],[0,0]]   #This is how the branch starting postions will be assigned, and updated.
for i in range(16):
    t1.fd(random.randint(25,100))
    t2.fd(random.randint(25,100))
    t3.fd(random.randint(25,100))
    t4.fd(random.randint(25,100))
    
    if (i % 2 == 0):        #determines the direction of rotation for the initial stalk
        t1.left(random.randint(20,60))
        t2.right(random.randint(20,60))
        t3.left(random.randint(20,60))
        t4.right(random.randint(20,60))
    else:
         t1.right(random.randint(20,100))
         t2.left(random.randint(20,100))
         t3.right(random.randint(20,100))
         t4.left(random.randint(20,100))
        
    if (i == 2):            #This sets the starting points for the first set of branches
         for j in range(1): #These branches are denoted t1b,t2b,t3b,t4b
             branchPos.insert(0,t1.pos())
             branchPos.insert(1,t2.pos())
             branchPos.insert(2,t3.pos())
             branchPos.insert(3,t4.pos())
    
         for k in range(1):
             t1b.goto(branchPos[0])
             t2b.goto(branchPos[1])
             t3b.goto(branchPos[2])
             t4b.goto(branchPos[3])
        
             t1b.pendown()
             t2b.pendown()
             t3b.pendown()
             t4b.pendown()
             
    #The following chunk determines how far the branches move forward.
    t1b.fd(random.randint(25,100))
    t2b.fd(random.randint(25,100))
    t3b.fd(random.randint(25,100))
    t4b.fd(random.randint(25,100))
    
    if (i % 2 == 0):        #The following two blocks change the rotation angle depending on if its even or odd.
        t1b.left(random.randint(20,60))
        t2b.right(random.randint(20,60))
        t3b.left(random.randint(20,60))
        t4b.right(random.randint(20,60))
    else:
         t1b.right(random.randint(20,100))
         t2b.left(random.randint(20,100))
         t3b.right(random.randint(20,100))
         t4b.left(random.randint(20,100))

    if (i == 5):    #This starts the second set of branches denoted t1c,t2c,t3c,t4c
         for j in range(1):
             branchPos.insert(0,t1.pos())
             branchPos.insert(1,t2.pos())
             branchPos.insert(2,t3.pos())
             branchPos.insert(3,t4.pos())
    
         for k in range(1):
             t1c.goto(branchPos[0])
             t2c.goto(branchPos[1])
             t3c.goto(branchPos[2])
             t4c.goto(branchPos[3])
        
             t1c.pendown()
             t2c.pendown()
             t3c.pendown()
             t4c.pendown()

    t1c.fd(random.randint(25,100))
    t2c.fd(random.randint(25,100))
    t3c.fd(random.randint(25,100))
    t4c.fd(random.randint(25,100))
    
    if (i % 2 == 0):        #This will be for the second set of branches; denoted t1c,t2c,t3c,t4c
        t1c.left(random.randint(20,60))
        t2c.right(random.randint(20,60))
        t3c.left(random.randint(20,60))
        t4c.right(random.randint(20,60))
    else:
         t1c.right(random.randint(20,100))
         t2c.left(random.randint(20,100))
         t3c.right(random.randint(20,100))
         t4c.left(random.randint(20,100))
    
    
turtle.done()

# t1.clear()
# t1b.clear()
# t1c.clear()
# t2.clear()
# t2b.clear()
# t2c.clear()
# t3.clear()
# t3b.clear()
# t3c.clear()
# t4.clear()
# t4b.clear()
# t4c.clear()