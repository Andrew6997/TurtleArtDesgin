import turtle
import random
import math
from Functions import *
turtle.colormode(255)
turtle.tracer(0)

turtle.bgcolor("black")

bob=turtle.Turtle()
Joe=turtle.Turtle()
Fal=turtle.Turtle()
Sam=turtle.Turtle()
Jam=turtle.Turtle()
Dav=turtle.Turtle()
Sai=turtle.Turtle()
Bib=turtle.Turtle()
Dev=turtle.Turtle()
Pur=turtle.Turtle()

bob.color("red")
Joe.color("red")
Fal.color(0,78,255)
Sam.color(0,55,255)
Dav.color(55,112,79)
Bib.color(255,165,0)
Dev.color(255, 0, 0)
Pur.color(255,69,0)	



move(Bib, 0, -400)
Bib.begin_fill()
Bib.circle(400)
Bib.end_fill()

move(Pur, 0, -350)
Pur.begin_fill()
Pur.circle(350)
Pur.end_fill()

move(Dev, 0, -300)
Dev.begin_fill()
Dev.circle(300)
Dev.end_fill()




move(Sai, -250,-250)
Sai.color("purple")
Sai.begin_fill()
square(Sai, 500)
Sai.end_fill()






for times in range(200):
    bob.fd(times *2)
    bob.lt(90)



for times in range(10):
    Sam.circle(times *12)

for times in range(8):
    Sam.lt(45)
    for times in range(10):
        Sam.circle(times *12)



for times in range(10):
    Joe.circle(times *10)

for times in range(8):
    Joe.lt(45)
    for times in range(10):
        Joe.circle(times *10)



for times in range(10):
    Dav.circle(times *10)

for times in range(8):
    Dav.lt(45)
    for times in range(10):
        Dav.circle(times *8)



for times in range(200):
    Jam.lt(90)
    Jam.fd(times *3)










