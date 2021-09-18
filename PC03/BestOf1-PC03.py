'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: 
May 29, 2020
PROGRAM DESCRIPTION GOES HERE <---------
'''
import turtle #import the library of commands that you'd like to use
import math #get a bunch of math commands

turtle.colormode(255)
sq = turtle.Turtle(shape="square")

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

#=======Add your code here======

panel.bgcolor("black") # set background color
#turtle.tracer(0) # turn off the animation  #uncomment along with line 33. ALWAYS update the panel!

#turtle.Turtle(visible=False) # create a turtle, make it invisible 

#===================
# YOUR CODE HERE!
R = 0
G = 0
B = 0
sq.color(R,G,B)

sq.goto(75,-150)

#looping twice

for u in range(12) :
    for i in range(12) :
        sq.color(((R+13*i),(G+12*i),(B+17*i)))
        sq.shapesize(4,4)
        sq.stamp()
        sq.left(30)
        sq.up()
        sq.forward(25)
        sq.down()
    
    sq.up()    
    sq.forward(100)
    sq.left(30)
    sq.down()

sq.up()
sq.goto(1000,1000)

#panel.update() # if the animation is off (line 25 is uncommented), then uncomment this line.
#===================
# turtle.done()
