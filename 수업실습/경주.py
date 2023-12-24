import turtle
import random
t1 = turtle.Turtle()
t2 = turtle.Turtle()

screen=turtle.Screen()
image1="D:/rabbit.gif"
image2="D:/turtle.gif"
screen.addshape(image1)
screen.addshape(image2)
t1.shape(image1)
t2.shape(image2)
t1.shapesize(4)
t2.shapesize(4)
t1.pensize(4)
t2.pensize(4)
t1.penup()
t2.penup()
t1.goto(-400, 100)
t2.goto(-400, -100)
t1.pendown()
t2.pendown()
for i in range(30):        
    a = random.randint(1, 50)             
    b = random.randint(1, 50)
    t1.forward(a)
    t2.forward(b)
