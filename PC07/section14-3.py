# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 12:59:42 2021

"""
#Turtle Graphics Game
import turtle
import math
import random

#Setup Screen
turtle.Screen()
turtle.bgcolor("green")

#Create player turtle
player = turtle.Turtle()
player.color("lightgreen")
player.shape("turtle")
player.turtlesize(4)
player.penup()
player.speed(0)

#Create ball goal
ball = turtle.Turtle()
ball.color("red")
ball.shape("circle")
ball.penup()
ball.turtlesize(1)
ball.setposition(random.randint(-400,400), random.randint(-400, 400))


#Set speed
speed = 1

def turnleft():
    player.left(30)
    
def turnright():
    player.right(30)

def increaseSpeed():
    global speed
    speed += 1
    

#Tie keyboard to turtle
turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(increaseSpeed, "Up")


while True:
    player.forward(speed)
    
    #Boundry check
    if player.xcor() > 400 or player.xcor() < -400:
            player.right(180)
    
    #Boundary check
    if player.ycor() > 400 or player.ycor() < -400:
            player.right(180)
    
    
    #collision checking. This part here I found on a video to allow the ball to disappear and reappear
    d =math.sqrt(math.pow(player.xcor()-ball.xcor(), 2) + math.pow(player.ycor()-ball.ycor(), 2))
    if d < 20:
            ball.setposition(random.randint(-400,400), random.randint(-400, 400))
