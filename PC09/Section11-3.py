"""
Created on Fri Nov  5 09:47:41 2021
In this game, the background is given a random color and shapes are randomly placed 
on the panel and you need to match the colrs! Make the shapes match the background
and you win!
@author: 

Objective: Match all the shapes to the background color.
Rules: The shapes will all need to be the background color to win, not just one or two.
Challange: The color of the shapes will be random each time the user must click it, 
           so you must continue to click it until you get the right color.
Interactions: To change the color of the circles, the user must click inside the shape.
"""
import turtle, random 
  
# Class for start screen  
class startButton(turtle.Turtle):  
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('green')
        self.shapesize(20)
        self.onclick(self.start)
        
        
    def start(self,x,y):
        panel.clear()
        Run()
        panel.update()
        turtle.color(chosenColor)
        
# Rules that are written on screen
def rules():  
        turtle.hideturtle()
        turtle.up()
        turtle.goto(-200,-215)
        turtle.color('black')
        turtle.write('Rules: Click each shape and make it the same color as the background.',font=50) 
        turtle.goto(-200,-230)
        turtle.write('Some colors will not change into the background.',font=50)
        turtle.goto(-200,-245)
        turtle.write('Click the green button to start',font=50)

# all the start-up stuff put into a setup function called starting
def starting():
    
    
    turtle.colormode(255)
    turtle.tracer(0)
        
    global panel
    panel = turtle.Screen()
    panel.clear()
    w = 600 # width of panel
    h = 600 # height of panel
    panel.setup(width=w, height=h)
    global running
    running = True
    
    
    
    
# list of colors for the shapes/fake shape. 
    global colors
    colors = ['blue', 'red', 'yellow', 'purple','pink','white','orange'] #color pallete
    global fakeColor
    fakeColor = ['cyan','green','brown','gold','mageneta']
    global shapes
    shapes = ['circle', 'square', 'triangle'] 
    global chosenColor
    chosenColor = 'white' #random background color
    print ('You must make all shapes ' + chosenColor)
    panel.bgcolor(chosenColor)
    

# Parent class of the shape
class Shape(turtle.Turtle): #Shape class
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.up()
        self.color(random.choice(colors))
        self.goto(self.x, self.y)
        self.onclick(self.click)
    
    # methods
    def click(self, x, y):
        global running
        self.color(random.choice(colors))
        
 
        
# Class that makes the circle shape
class Circle(Shape):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.shape('circle')
        self.color(random.choice(colors))
        self.up()
        self.shapesize(5)
        self.goto(self.x,self.y)

# Class that makes the triangle shape
class Triangle(Shape):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.shape('triangle')
        self.color(random.choice(colors))
        self.up()
        self.shapesize(5)
        self.goto(self.x,self.y)

# Class that makes the square shape
class Square(Shape):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.shape('square')
        self.color(random.choice(colors))
        self.up()
        self.shapesize(5)
        self.goto(self.x,self.y)
        
# Class that makes the 'fake' shape
class Enemy(Shape):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.shape(random.choice(shapes))
        self.color(random.choice(colors))
        self.up()
        self.shapesize(5)
        self.goto(self.x,self.y)
    
    def click(self,x,y):
        global running
        self.color(random.choice(fakeColor))
        

# puts all the stuff that calls the classes and puts it into a run function        
def Run():        
         
# Making the shapes below
    circle = Circle(random.randint(-250, 250), random.randint(-250,250))
    
    triangle = Triangle(random.randint(-250, 250), random.randint(-250,250))
    
    square = Square(random.randint(-250, 250), random.randint(-250,250))
   
    enemy = Enemy(random.randint(-250,250),random.randint(-250,250))
   
            
# Win conditions
    def finalEnd():
        endgameCircle = False
        endgameTriangle = False
        endgameSquare = False
        
        if circle.color()[0] == chosenColor:
            endgameCircle = True
        else:
            return
                    

        if triangle.color()[0] == chosenColor:
            endgameTriangle = True
        else:
            return
                    

        if square.color()[0] == chosenColor: 
            endgameSquare = True
        else:
            return
                    
        
        global running
        if endgameCircle and endgameTriangle and endgameSquare is True:
            turtle.hideturtle()
            turtle.write("You Win!",font='400')
        else:
            return   
    
    while running:
        
        finalEnd() 
        
        panel.update()
    
starting()
rules()
gameStart = startButton()
turtle.mainloop()

'''Comment made by XX: It is a fun little game but I think it would be more fun
if there were more shapes. There was only 3 so it didn't take too long to win. I liked
that there was a mystery shape that was there as a distraction though. It would also be 
fun if you were competing against another person or maybe timer or something. Overall 
I enjoyed it and the quality of life has improved since last time with a start button,
rules, and a winning statement.'''
