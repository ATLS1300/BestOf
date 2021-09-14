#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: YOUR NAME
May 29, 2020
'''

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
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======




#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
#turtle.done()
turtle.up()
turtle.goto(-80,210)
turtle.pendown()
turtle.pensize(3)
turtle.begin_fill()
turtle.left(90)
turtle.forward(150)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(150)
turtle.right(90)
turtle.end_fill()
turtle.forward(150)
turtle.right(180)
turtle.forward(200)
# ^ All top hat

turtle.begin_fill()
turtle.right(90)
turtle.forward(25)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(25)
turtle.end_fill()
turtle.right(90)
turtle.forward(50)
turtle.pensize(1)
turtle.color("gray100")
turtle.forward(100)
turtle.color("gray0")
turtle.pensize(3)

# ^ bottom of top hat

turtle.up()
turtle.goto(111,-90)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("burlywood4")
turtle.right(30)
turtle.forward(45)
turtle.right(30)
turtle.forward(75)
turtle.right(30)
turtle.forward(100)
turtle.right(60)
turtle.forward(60)
turtle.right(30)
turtle.forward(50)
turtle.forward(50)
turtle.right(30)
turtle.forward(60)
turtle.right(60)
turtle.forward(100)
turtle.right(30)
turtle.forward(32)
turtle.right(65)
turtle.forward(50)
turtle.left(50)
turtle.forward(30)
turtle.left(25)
turtle.forward(30)
turtle.left(50)
turtle.forward(15)
turtle.right(135)
turtle.forward(40)
turtle.left(90)
turtle.forward(15)
turtle.end_fill()

#^ outline of money bag


turtle.up()
turtle.goto(115,-210)
turtle.down()
turtle.begin_fill()
turtle.fillcolor("chartreuse2")
turtle.left(15)
turtle.forward(20)
turtle.left(45)
turtle.forward(20)
turtle.left(45)
turtle.forward(20)
turtle.left(45)
turtle.forward(20)
turtle.left(45)
turtle.forward(30)
turtle.left(45)
turtle.forward(20)
turtle.left(45)
turtle.forward(20)
turtle.right(90)
turtle.forward(20)
turtle.right(90)
turtle.forward(20)
turtle.right(90)
turtle.forward(10)
turtle.left(90)
turtle.forward(15)
turtle.left(90)
turtle.forward(20)
turtle.left(45)
turtle.forward(20)
turtle.left(45)
turtle.forward(20)
turtle.left(45)
turtle.forward(25)
turtle.left(45)
turtle.forward(25)
turtle.left(45)
turtle.forward(20)
turtle.left(45)
turtle.forward(25)
turtle.right(90)
turtle.forward(20)
turtle.right(90)
turtle.forward(22)
turtle.right(90)
turtle.forward(10)
turtle.left(90)
turtle.forward(13)
turtle.end_fill()
# ^S

turtle.up()
turtle.goto(105,-150)
turtle.down()
turtle.pensize(4)
turtle.color("DarkGreen")
turtle.right(90)
turtle.forward(150)
turtle.up()
turtle.goto(85,-150)
turtle.down()
turtle.forward(150)

# ^ Lines going down

turtle.up()
turtle.goto(-55,270)
turtle.down()
turtle.colormode(255)
turtle.pencolor(102,204,255)
turtle.circle(25)
