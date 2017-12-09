# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 16:38:32 2017

@author: takis

turtle.shapesize(stretch_wid=None, stretch_len=None, outline=None)
"""
import random
import turtle as t

t.colormode(255)
t.setup(width=800, height=800, startx=400, starty=50)
t.title("Bubblesort with Turtle")
t.screensize(550,450)


def createBarTurtle(size, tPosition):
    t1 = t.Turtle()
    t1.pu()
    t1.shape("square")
#    t1.color("grey")
    t1.pen(fillcolor=randColor(), outline=2)
    t1.shapesize(size, 1) # square-->rectangle
#    print(t1.shapesize(), end=" ")
    # align blocks by the bottom edge
    y = -300
    y_offset = 0
    y_offset = size * 20/2
#    print("y_offset:", y_offset)
    y = y + y_offset
    x = -200 + 20/2 + tPosition + (25*tPosition)
    t1.setpos(x, y)
#    t1.write(size ,align="left", font=("Courier", 20, "bold"))

    return t1


def Axes():
    t.ht()
    t.pd()
    t.goto(-200,0)
    t.goto(200,0)
    t.pu()
    t.goto(0,0)
    t.pd()
    t.goto(0,-200)
    t.goto(0,200)
    t.pu()
    t.ht()

def randColor():
    r = random.randint(0,254)
    g = random.randint(0,254)
    b = random.randint(0,254)
    myColor = (r,g,b)
#    print(r,g,b)
#    myColor="blue"
    return myColor

t.reset()
t.delay(20)
tList= []
count = 0
sizeList = []
#sizeList = [10,5,7]
#sizeList = [20,14,2,11,7,9,4,1,30,18,3,]

## Random SizeList
randomSize = random.randint(10,30)
for i in range(randomSize) :
    x = random.randint(1,20)
    if x not in sizeList:
        sizeList.append(x)

## Display Axes
#Axes()

## Write Message of List Dimension
t.ht()
t.up()
t.goto(-200,300)
t.write("Random list of "+str(len(sizeList))+" elements", font="Arial 20")

# Create turtles as Bars
for i in sizeList:
    tPosition = i
    tList.append(createBarTurtle(i, sizeList.index(i)))
    count+=1


for j  in range(len(tList)):
    for i in range(len(tList)):
          print(tList[i].turtlesize()[0], tList[i].pos())
          ## Check limits of list
          if( i+1 < len(tList) ):
              if( tList[i].turtlesize()[0] > tList[i+1].turtlesize()[0]):
                  print("SWAP !", tList[i].turtlesize()[0],tList[i+1].turtlesize()[0] )
                  ## Swap COORDINATES
                  tempCorx = tList[i+1].xcor()
                  smallCorx = tList[i].xcor()
                  bigCorx = tempCorx
                  tList[i].goto(bigCorx,  tList[i].ycor())
                  tList[i+1].goto(smallCorx, tList[i+1].ycor())
                  ## Swap turtles
                  tempTurtle = tList[i+1]
                  tList[i+1] = tList[i]
                  tList[i] = tempTurtle

## Write Message of Completion
t.pu()
t.goto(-200,  -350)
t.write("Bubble-sort Finished !!!", font="Arial 20")
t.mainloop()
t.exitonclick()