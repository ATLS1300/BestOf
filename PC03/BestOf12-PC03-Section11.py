'''
ATLAS 1300
Author
Sep 14 2021
PC03 Zoom Background
'''


from turtle import *
import math

def turtleTeleport(x,y):
    #easily move turtle to different points
    up()
    goto(x,y)
    down()

panel = Screen()
speed(0)
w = 600
h = 600

panel.setup(width=w,height=h)

panel.bgcolor(0,0,0)

Turtle(visible=True)
color('white')
def drawHeart():
    down()
    for angle in range(0,180):
        angle = math.radians(angle)
        x = 300*(1/6*math.sin(2*angle)*(1 + math.cos(80*angle))*(1-1/12*(math.sin(2*angle))**8))
        y = 300*(-1/2*(2*angle/math.pi - 1)**2 + 1/7*math.sin(2*angle)*(math.sin(80*angle)**3))
        goto(x,y)

drawHeart()
