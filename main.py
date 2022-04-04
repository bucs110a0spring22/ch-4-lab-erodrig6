import turtle
import math
########### Your Code here ##############
# You should only have functions here
# If you have anything outside of a function, 
# then you do not fully understand functions
# and should review how they work or ask for help
def changeShape(turt):
  shapeRequested = input("To select a different turtle shape, please input the corresponding number\n1.) Square\n2.) Arrow\n3.) Circle\n4.) Turtle\n")
  if shapeRequested == "1":
    turt.shape('square')
    print("The new shape is:\nSquare!")
  elif shapeRequested == "2":
    turt.shape('arrow')
    print("The new shape is:\nArrow!")
  elif shapeRequested == "3":
    turt.shape('circle')
    print("The new shape is:\nCircle!")
  elif shapeRequested == "4":
    turt.shape('turtle')
    print("The new shape is:\nTurtle!")
  else:
    print("I'm sorry, that input is not recognized.")

def changeSpeed(turt):
  speedRequested = input("Select a speed, 1 through 10. The higher the number, the faster the speed. Only integer values are acceptable.\n")
  speedInt = int(speedRequested)
  if speedInt > 0 and speedInt < 11:
    turt.speed(speedInt)
  else:
    print("Invalid.")

def drawSineCurve(turt):
  turt.penup()
  turt.goto(-360, math.sin(math.radians(-360)))
  turt.pendown()
  for i in range(-360, 361):
    turt.goto(i, math.sin(math.radians(i)))

def drawCosineCurve(turt):
  turt.penup()
  turt.goto(-360, math.cos(math.radians(-360)))
  turt.pendown()
  for i in range(-360, 361):
    turt.goto(i, math.cos(math.radians(i)))

def drawTangentCurve(turt):
  turt.penup()
  turt.goto(-360, math.tan(math.radians(-360)))
  turt.pendown()
  for i in range(-360, 361):
    turt.goto(i, math.tan(math.radians(i)))
  
def setupWindow():
    wn = turtle.setworldcoordinates(-360, -1, 360, 1)

def setupAxis(turtle_axis):
 ### turtle_axis.shape('turtle')
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
    changeSpeed(dart)
    changeShape(dart)
    #dart.speed(0)
    #drawSineCurve(dart)

    #Part B
    setupWindow()
    setupAxis(dart)
    #dart.speed(0)
    drawSineCurve(dart)
    drawCosineCurve(dart)
    drawTangentCurve(dart)
    wn.exitonclick()
main()
    