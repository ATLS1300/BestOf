"""
Created on Thu Sep 15 11:39:56 2020
PC04 
@author: 

*********  **********
This generative art pieace uses multiple turtles to create a fun geometric design 
with randomized colors that are changed for every running of the code 


"""
import turtle
import math, random

turtle.colormode(255)
# turtle.tracer(0) # uncomment this line to turn off turtle's animation. You must update the image yourself using panel.update() (line 42)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 700 # width of panel
h = 700 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
panel.bgcolor(0,0,0)

#You can experiment by making 

# You must make 2 turtle variables
# You must use 2 for loops (a nested for loop counts as 2!)
# You must use at least 1 random element (something from the random library)
# Don't forget to comment your code! (what does each for loop do? What does the random function you'll use do?)

# =============== ADD YOUR CODE BELOW! =================
nameAnswer = input("            Hello Artist! It's time to create your own unique piece! but first, what is your name? ")

#COMMENTS
#every color is unique I used the randomint function to change the RGB colorsfor every line the turte draws


turtle.up()
turtle.color(255,255,255)
turtle.goto(-350,345)
turtle.speed(10) 
turtle.pensize(5)

yValue = 345

for iteration in range(20):
    redRandom = random.randint(100, 240)
    blueRandom = random.randint(75,200)
    turtle.down()
    turtle.color(redRandom,40,blueRandom)
    turtle.setheading(0)
    turtle.forward(500)
    turtle.left(60)          #angle
    turtle.forward(50)
    turtle.right(120)       #angle
    turtle.forward(50)
    turtle.left(60)          #angle
    turtle.forward(150)
    turtle.up()
    turtle.goto(-350, yValue)
    yValue -= 15

# hole filler 
turtle.goto(150,60)
turtle.color(redRandom,40,blueRandom)
turtle.down()
turtle.setheading(0)
turtle.left(60)          #angle
turtle.forward(50)
turtle.right(120)       #angle
turtle.forward(50)
turtle.left(60)          #angle
turtle.forward(150)
turtle.backward(200)

ricky = turtle.Turtle()
turtle.up()

xValueTriangle = -358                       #THESE
yValueTriangle = 60
ricky.pensize(5)
ricky.speed(10)



ricky.goto(-358,60)  #DONT FORGET TO CHANGE ^^^
for iteration in range(20):
    redRandom = random.randint(75, 175)
    blueRandom = random.randint(125,250)
    ricky.down()
    ricky.color(redRandom,70,blueRandom)
    ricky.setheading(0)
    ricky.forward(500)
    ricky.right(120)
    ricky.forward(500)
    ricky.up()
    xValueTriangle -= 25
    yValueTriangle -= 15
    ricky.goto(xValueTriangle,yValueTriangle)



#======================SQUARES==============

square = turtle.Turtle()
square.color(255,255,255)
square.pensize(5)
square.speed(10)

square.up()


positions = ((335,45),(335,-43),(335,-131),(335,-219),(247,45),(247,-43),(247,-131),(247,-219),(247,-307),(333,-307))

i = 0

for squaresloop in range(10):
        blueRandom2 = random.randint(50,250)
        greenRandom = random.randint(50,175)
        square.color(50,greenRandom,blueRandom2)
        square.goto(positions[i])
        square.setheading(0)
        i += 1
        square.down()
        square.right(90)
        square.forward(73)
        square.right(90)
        square.forward(73)
        square.right(90)
        square.forward(73)
        square.right(90)
        square.forward(73)
        square.up()
        square.right(135)
        square.forward(21.21)
        square.down()
        square.left(45)
        square.forward(43)
        square.right(90)
        square.forward(43)
        square.right(90)
        square.forward(43)
        square.right(90)
        square.forward(43)
        square.right(90)
        square.up()

turtle.up()
turtle.goto(30,-345)
turtle.write("-"+ nameAnswer,move='false',align='center',font=('Arial',40,'normal'))


# panel.update() # uncomment this if you've turned off animation (line 26). I recommend leaving this outside of loops, for now.
# =================== CLEAN UP =========================
# uncomment the line below when you are finished with your code (before you turn it in)
turtle.done()
