#!/usr/bin/env python3
"""       turtle-example-suite:

         tdemo_minimal_hanoi.py

A minimal 'Towers of Hanoi' animation:
A tower of 6 discs is transferred from the
left to the right peg.

An imho quite elegant and concise
implementation using a tower class, which
is derived from the built-in type list.

Discs are turtles with shape "square", but
stretched to rectangles by shapesize()
 ------------------------------------------

Tower of Hanoi puzzle with n disks can be solved in minimum (2**n)−1 steps.
A puzzle with 3 disks has taken 23 - 1 = 7 steps.

We divide the stack of disks in two parts.
The largest disk (nth disk) is in one part and
all other (n-1) disks are in the second part.

Step 1 − Move n-1 disks from source to aux
Step 2 − Move nth disk from source to dest
Step 3 − Move n-1 disks from aux to dest

A recursive algorithm for Tower of Hanoi can be driven as follows −

START
Procedure Hanoi(disk, source, dest, aux)

   IF disk == 1, THEN
      move disk from source to dest
   ELSE
      Hanoi(disk - 1, source, aux, dest)     // Step 1
      move disk from source to dest          // Step 2
      Hanoi(disk - 1, aux, dest, source)     // Step 3
   END IF

END Procedure
STOP
---------------------------------------------------------
"""

from turtle import *

class Disc(Turtle):
    def __init__(self, n):
        Turtle.__init__(self, shape="square", visible=False)
        self.speed(1)
        self.pu()
        self.shapesize(1.5, n*1, 2) # square-->rectangle
#        self.fillcolor(n/6., 0.1, 1-n/6.)
        self.fillcolor(n/10., 0.4, 1-n/10.)
        self.st()

class Tower(list):
    "Hanoi tower, a subclass of built-in type list"
    def __init__(self, x, name):
        "create an empty tower. x is x-position of peg"
        self.x = x
        self.name = name
        goto(x, -200)
        write(self.name,  align="center", font=("Consolas", 10, "bold"))
    def push(self, d):
        d.setx(self.x)
        d.sety(-150+34*len(self))
        self.append(d)
    def pop(self):
        d = list.pop(self)
        d.sety(150)
        return d

#def hanoi(n, from_, with_, to_):
#    if n > 0:
#        hanoi(n-1, from_, to_, with_)
#        to_.push(from_.pop())
#        hanoi(n-1, with_, from_, to_)

def hanoi(n, source, aux , destination ):
    global numOfCalls

    print("n= " , n)

    if n == 1:
         print("IF n==",n , "Pop & Push disk")
         destination.push(source.pop())

    else:
        numOfCalls += 1
        print("No.:",numOfCalls, "RECURSIVE CALL of hanoi")
        print("DIRECTION : From SOURCE -> AUX")
        hanoi(n-1, source, destination, aux)
        print("ELSE n=",n , "Pop & Push disk")
        destination.push(source.pop())
        numOfCalls += 1
        print("No.:",numOfCalls, "RECURSIVE CALL of hanoi - AFTER POP-PUSH of BIGEST disk !!!")
        print("Change DIRECTION ! From AUX -> Source")
##        onkey(pause, 'Enter')
##        listen()
#        input("Press Enter to continue...")
        hanoi(n-1, aux, source, destination)


def play():
    onkey(None,"space")
#    clear()
    goto(0, -250)
    pencolor("white")
    write("Press <Spacebar> to start game",
          align="center", font=("Consolas", 16, "bold"))
    pencolor("Green")
    write("Running ... ",
          align="center", font=("Consolas", 16, "bold"))

#    try:
    hanoi(numOfDiscs, t1, t2, t3)
    write("Problem Solved !",  align="center", font=("Consolas", 16, "bold"))
#        write("press STOP button to exit",
#              align="center", font=("Courier", 16, "bold"))
#    except Terminator:
#        pass  # turtledemo user pressed STOP

def main():

    global t1, t2, t3, numOfDiscs, numOfCalls
    numOfDiscs = 2
    numOfCalls = 0
    ht(); penup(); goto(0, -225)   # writer turtle
    t1 = Tower(-250, "Source")
    t2 = Tower(0, "Auxiliary")
    t3 = Tower(250, "Destination")
    # make tower of 6 discs
    for i in range(numOfDiscs,0,-1):
        t1.push(Disc(i))
#    # prepare spartanic user interface ;-)
    goto(0, -250)
    write("Press <Spacebar> to start game",
          align="center", font=("Consolas", 16, "bold"))
    onkey(play, "space")
    listen()
    return "EVENTLOOP"

if __name__=="__main__":
    msg = main()
    print(msg)
    mainloop()
