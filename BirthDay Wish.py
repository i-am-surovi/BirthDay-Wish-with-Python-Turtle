import turtle
happy = turtle.Screen()
happy.bgcolor("black")
turtle = turtle.Turtle()
turtle.shape("circle")
turtle.color("yellow")
turtle.width(7)
colors=["red","green","blue","yellow","orange red"]

import time
time.sleep(20)

def draw_happy(i,x,y):
    turtle.pencolor("linen")
    turtle.color(colors[i%7])
    turtle.begin_fill()
    turtle.lt(70)
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.circle(33)
    turtle.end_fill()

def f1():
  for i in range(7):
    turtle.pensize(5)
    turtle.pencolor('light blue')
    turtle.color(colors[i%19])
    turtle.begin_fill()
    turtle.left(330)
    turtle.forward(55)
    turtle.begin_fill()
    turtle.rt(110)
    turtle.circle(33)
    turtle.end_fill()
    turtle.rt(11)
    turtle.backward(33)
    turtle.end_fill()

def cake(x,y):
   turtle.fd(x)
   turtle.rt(90)
   turtle.fd(y)
   turtle.rt(90)
   turtle.fd(x)
   turtle.rt(90)
   turtle.fd(y)

def candle(x):
   turtle.fd(x)

def move(x,y):
   turtle.up()
   turtle.setposition(0,0)
   turtle.setheading(90)
   turtle.rt(90)
   turtle.fd(x)
   turtle.lt(90)
   turtle.fd(y)
   turtle.pendown()

def mov(x,y):
   turtle.up()
   turtle.setposition(0,0)
   turtle.setheading(90)
   turtle.lt(90)
   turtle.fd(x)
   turtle.rt(90)
   turtle.fd(y)
   turtle.pendown()

def A(size):
  turtle.rt(19)
  turtle.forward(size)
  turtle.rt(141)
  turtle.fd(size)
  turtle.backward(size/2)
  turtle.rt(105)
  turtle.fd(int(size/3))

def B(size):
   turtle.forward(size)
   turtle.rt(90)
   for i in range(18):
      turtle.rt(9)
      turtle.fd(size//20)
   for i in range(18):
      turtle.rt(size//5)
      turtle.backward(size//20)

def C(size):
    turtle.rt(140)
    turtle.up()
    for i in range(0,int(size/4)):
        turtle.fd(int(size/20))
        turtle.lt(5)
    turtle.down()
    for i in range(int((int(size/4)*3))):
        turtle.back(int(size/20))
        turtle.rt(5)

def D(size):
   turtle.fd(size)
   turtle.rt(90)
   turtle.fd(size//10)
   for i in range(13):
      turtle.rt(13)
      turtle.fd(size//8)

def E(size):
    turtle.rt(90)
    turtle.fd(int(size/3))
    turtle.back(int(size/3))
    turtle.left(90)
    turtle.fd(size/2)
    turtle.rt(90)
    turtle.fd(int(size/3))
    turtle.back(int(size/3))
    turtle.lt(90)
    turtle.fd(size/2)
    turtle.rt(90)
    turtle.fd(int(size/3))

def F(size):
    turtle.fd(size)
    turtle.rt(90)
    turtle.fd(size//2)
    turtle.backward(size//2)
    turtle.rt(90)
    turtle.fd(size//3)
    turtle.lt(90)
    turtle.fd(size//3)

def G(size):
      turtle.penup()
      turtle.fd(size//2)
      turtle.pendown()
      turtle.lt(90)
      turtle.fd(size//3)
      turtle.backward(size//3)
      turtle.lt(90)
      for _ in range(size):
        turtle.rt(5)
        turtle.fd(2)

def H(size):
   turtle.fd(size)
   turtle.backward(size//2)
   turtle.rt(90)
   turtle.fd(size//2)
   turtle.lt(90)
   turtle.fd(size//2)
   turtle.backward(size)

def I(size):
   turtle.fd(size)
   turtle.rt(90)
   turtle.circle(size//8)

def J(size):
    turtle.lt(180)
    turtle.fd(size/1.2)
    for i in range(13):
        turtle.rt(13)
        turtle.fd(int(size/21))
    turtle.ht()

def K(size):
    turtle.fd(size)
    #turtle.width(9)
    turtle.backward(size//2)
    turtle.rt(60)
    turtle.fd(size//1.5)
    turtle.backward(size//2)
    turtle.rt(80)
    turtle.fd(size//1.3)

def L(size):
    turtle.rt(90)
    turtle.fd(int(size/2))
    turtle.back(int(size/2))
    turtle.lt(90)
    turtle.fd(size)

def M(size):
    turtle.fd(int(size/2))
    turtle.rt(135)
    turtle.fd(int(size/3))
    turtle.lt(90)
    turtle.fd(int(size/3))
    turtle.rt(135)
    turtle.fd(int(size/2))

def N(size):
    turtle.fd(size)
    turtle.rt(150)
    turtle.fd(size+int(size/6))
    turtle.lt(150)
    turtle.fd(size)

def O(size):
    turtle.right(90)
    turtle.circle(size//2)

def P(size):
   turtle.fd(size)
   turtle.rt(90)
   turtle.fd(size//8)
   for i in range(8):
       turtle.rt(20)
       turtle.fd(size//9)

def Q(size):
    turtle.circle(100)
    for i in range(0,int(size/6)):
        turtle.lt(9)
        turtle.fd(5)
    turtle.back(int(size))

def R(size):
   turtle.fd(60)
   turtle.rt(90)
   turtle.fd(7)
   for i in range(15):
      turtle.rt(12)
      turtle.fd(3)
   turtle.lt(120)
   turtle.fd(40)

def S(size):
    turtle.rt(90)
    for i in range(0,5):
        if i<3:
            turtle.fd(size/2)
            turtle.lt(90)
            if i==2:
                turtle.rt(90)
        else:
            turtle.right(90)
            turtle.fd(size/2)

def T(size):
   turtle.fd(size)
   turtle.rt(90)
   turtle.fd(size//2)
   turtle.backward(size//2)

def U(size):
  turtle.rt(90)
  for i in range(size//10):
    turtle.lt(15)
    turtle.fd(size//10)
  turtle.fd(size//2)
  turtle.back(size//2)

  for i in range(size//10):
    turtle.rt(13)
    turtle.back(size//10)
  turtle.lt(5)
  for i in range(size//10):
    turtle.rt(17)
    turtle.back(size//10)
  turtle.back(size//2)

def V(size):
  turtle.right(20)
  turtle.fd(size)
  turtle.back(size)
  turtle.lt(40)
  turtle.fd(size)
  turtle.back(size)

def W(size):
  turtle.lt(20)
  turtle.fd(size)
  turtle.back(size)
  turtle.rt(50)
  turtle.fd(size//1.5)
  turtle.lt(60)
  turtle.backward(size//1.5)
  turtle.rt(50)
  turtle.fd(size)

def X(size):
    turtle.rt(30)
    turtle.fd(size)
    turtle.backward(size//2)
    turtle.rt(120)
    turtle.fd(size//2)
    turtle.backward(size)

def Y(size):
   turtle.fd(size)
   turtle.left(60)
   turtle.fd(size//2)
   turtle.backward(size//2)
   turtle.rt(90)
   turtle.fd(size//1.5)

def Z(size):
    turtle.lt(90)
    turtle.fd(size)
    turtle.rt(135)
    turtle.fd(size+(size//2))
    turtle.lt(135)
    turtle.fd(size)

turtle.speed(19)

from turtle import *
from random import randint

def Spiral():
    x=1
    turtle.speed(0)
    while x<200:
      turtle.pencolor("yellow")
      turtle.fd(10+x)
      turtle.rt(90.991)
      x = x+1

def triangle(size):
  turtle.color(colors[5%3])
  turtle.begin_fill()
  for i in range(3):
      turtle.pencolor(colors[i%4])
      turtle.left(120)
      turtle.fd(size)
  turtle.end_fill()

def triflow():
    for i in range(12):
        triangle(140)
        turtle.left(30)
        turtle.fd(10)
        triangle(151)

def spiral():
  for i in range(60):
    turtle.pencolor("yellow")
    turtle.circle(2*i)
    turtle.circle(-2*i)
    turtle.left(i)

def draw_leaf(leaf):       #creates leaf function
      for i in range(0,2):
            leaf.forward(90)
            leaf.right(40+i)
            leaf.left(40+i)
            for j in range(0,21):
                  leaf.right(3)
                  leaf.forward(5)
            leaf.right(145)

def draw_flower(pen):
      turtle.speed(12)
      for i in range(0,5):
        pen.color(colors[i%8])
        pen.begin_fill()
        draw_leaf(pen)
        pen.end_fill()
        pen.right(10)


turtle.width(1)
mov(480,180)
Spiral()
mov(-480,180)
Spiral()

mov(-450,-250)
draw_flower(turtle)
mov(450,-250)
draw_flower(turtle)

#Cake maker section
turtle.shape('turtle')
mov(120,40)
turtle.color("dark orange")
turtle.begin_fill()
cake(40,120)
turtle.end_fill()
mov(110,75)
turtle.color("hot pink")
turtle.begin_fill()
cake(40,100)
turtle.end_fill()
mov(100,110)
turtle.color("blanched almond")
turtle.begin_fill()
cake(40,80)
turtle.end_fill()
mov(30,150)
turtle.width(11)
turtle.pencolor("red")
turtle.circle(7)
# #end Of Cake Section

mov(80,152)
turtle.width(5)
turtle.pencolor("yellow")
candle(20)
move(-60,152)
candle(20)
#Name section
turtle.speed(12)
turtle.width(12)
turtle.pencolor("lime")
mov(160,200)
D(60)
mov(110,200)
E(60)
mov(70,200)
A(60)
mov(10,200)
R(60)
mov(-70,200)

# #happybithday
turtle.pencolor("cyan")
turtle.width(13)
mov(260,-60)
H(100)
turtle.width(7)
mov(190,-60)
A(65)
mov(135,-60)
P(60)
mov(100,-60)
P(60)
mov(52,-60)
Y(60)
mov(28,-60)

B(60)
move(12,-60)
I(60)
move(36,-60)
R(60)
move(80,-60)
T(100)
move(102,-60)
H(60)
move(150,-60)

turtle.pencolor('hotpink')
D(200)
move(160,-60)
A(60)
move(220,-60)
Y(60)

turtle.width(4)
turtle.pencolor('white')
move(-10,-140)
turtle.write("(22 December, 2023)",font="arial 25",align="center")
move(10,-170)
turtle.pencolor('yellow')
turtle.width(5)
turtle.write("Congratulations for advancing one year ahead to get grey hair and wrinkles...",font="TimesNewRoman 14",align="center")
move(10, -190)
turtle.write("Wait for me!!",font="TimesNewRoman 14",align="center")
move(10, -280)
happy.exitonclick()