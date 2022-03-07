import turtle
import math
########### Your Code here ##############
# You should only have functions here
# If you have anything outside of a function, 
# then you do not fully understand functions
# and should review how they work or ask for help

def drawSineCurve(meg):
  win = turtle.Screen()
  meg.penup()
  meg.goto(-360, math.sin(math.radians(-360)))
  meg.pendown()
  for i in range(-360, 361):
    meg.goto(i, math.sin(math.radians(i)))

def drawCosineCurve(meg):
  win = turtle.Screen()
  meg.penup()
  meg.goto(-360, math.cos(math.radians(-360)))
  meg.pendown()
  for i in range(-360, 361):
    meg.goto(i, math.cos(math.radians(i)))

def drawTangentCurve(meg):
  win = turtle.Screen()
  meg.penup()
  meg.goto(-360, math.tan(math.radians(-360)))
  meg.pendown()
  for i in range(-360, 361):
    meg.goto(i, math.tan(math.radians(i)))
  
def setupWindow(win):
    win = turtle.setworldcoordinates(-360, -1, 360, 1)

def setupAxis(turtle_axis):
  turtle_axis.shape('turtle')
  for i in range(2):
    turtle_axis.goto(0, 0)
    turtle_axis.right(90)
    turtle_axis.forward(1)
    turtle_axis.goto(0,0)
    turtle_axis.right(90)
    turtle_axis.forward(360)
    turtle_axis.goto(0, 0)
##########  Do Not Alter Any Code Past Here ########
def main():
    #Part A
    wn = turtle.Screen()
    wn.tracer(5)
    dart = turtle.Turtle()
    dart.speed(0)
    drawSineCurve(dart)

    #Part B
    setupWindow(wn)
    setupAxis(dart)
    dart.speed(0)
    drawSineCurve(dart)
    drawCosineCurve(dart)
    drawTangentCurve(dart)
    wn.exitonclick()
main()
