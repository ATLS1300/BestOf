"""
Created on Thu Sep 15 11:39:56 2020
PC04 start code
@author:

********* HEY, READ THIS FIRST **********

The title of this piece is "Squarel", sort of like a mix between the word "square" and "spiral." NOT TO BE CONFUSED WITH SQUIRREL, RUDE!
I was inspired to try some advanced concepts like modulo and if else to see how it impacted the art. 
The randomly generated corners center the attention on the spiral and fit with the only-square theme.
My hope is that the viewer of this piece feels a sense of chaotic nostalgia, reminscient of the
dreams that spiraled out of their control and reach once they hit adulthood. 
"""
import turtle
import random

turtle.colormode(255) #plz note: this color mode has been having issues and I have no clue why

#turtle.tracer(0) # uncomment this line to turn off turtle's animation. You must update the image yourself using panel.update() (line 42)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 600 # width of panel
h = 600 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making 
turtle.speed(0)
# You must make 2 turtle variables
# You must use 2 for loops (a nested for loop counts as 2!)
# You must use at least 1 random element (something from the random library)
# Don't forget to comment your code! (what does each for loop do? What does the random function you'll use do?)

# =============== ADD YOUR CODE BELOW! =================
#create square turtle
square=turtle.Turtle()
#function variables
lengthLow = 15
iterationsA = 160

#create color list from coolors.com
darkLiver = (88,75,83)
copperRose = (157,92,99)
periwinkleCrayola = (214,227,248)
seashell = (254,245,239)
desertSand = (228,187,151)
tealBlue = (59,112,128) #for modulo
colorList = [darkLiver, copperRose, periwinkleCrayola, desertSand]*100

square.penup()
square.goto(-20,0) #center spiral
#create cool square spiral thingymajingy
for i in range(iterationsA):
    square.pendown()
    square.begin_fill()
    for z in range(3):
        if i%9==0 or i%6==0 : #add the teal blue color in
            square.color(tealBlue)
        else: 
            square.color(random.choice(colorList))
        square.forward(lengthLow) #square length
        square.right(90)
    square.end_fill()
    square.penup()
    if i%3==0 : #the basis of the shape of this pattern, twist and movement
        square.forward(i+42)
    else:
        square.forward(i+9)
    if i%9==0 :
        square.right(6) #turn
    square.right(7)
square.penup()

#create new turtle
new=turtle.Turtle()
new.penup()
#how many iterations of squares
iterationsB= (14)

#set background to better white
turtle.bgcolor(seashell)

#corner squares top left
for i in range(iterationsB): #randomly generates the squares
    new.goto(random.randint(-300,-175),random.randint(175,300))
    new.begin_fill()
    size = random.randint(15,35)
    for i in range(4): #creates actual square
        new.pendown()
        new.color(random.choice(colorList))
        new.forward(size)
        new.right(90)
        new.penup()
    new.end_fill()

#corner squares top right
for i in range(iterationsB):
    new.goto(random.randint(175,300),random.randint(175,300))
    new.begin_fill()
    size = random.randint(15,35)
    for i in range(4): #creates actual square
        new.pendown()
        new.color(random.choice(colorList))
        new.forward(size)
        new.right(90)
        new.penup()
    new.end_fill()

#corner squares bottom right
for i in range(iterationsB):
    new.goto(random.randint(175,300),random.randint(-300,-175))
    new.begin_fill()
    size = random.randint(15,35)
    for i in range(4): #the actual square
        new.pendown()
        new.color(random.choice(colorList))
        new.forward(size)
        new.right(90)
        new.penup()
    new.end_fill()

#corner squares bottom left
for i in range(iterationsB):
    new.goto(random.randint(-300,-175),random.randint(-300,-175))
    new.begin_fill()
    size = random.randint(15,35)
    for i in range(4): #the actual square
        new.pendown()
        new.color(random.choice(colorList))
        new.forward(size)
        new.right(90)
        new.penup()
    new.end_fill()
# panel.update() # uncomment this if you've turned off animation (line 26). I recommend leaving this outside of loops, for now.
# =================== CLEAN UP =========================
# uncomment the line below when you are finished with your code (before you turn it in)
turtle.done()
