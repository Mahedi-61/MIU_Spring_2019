'''@Author     : Md Mahedi Hasan
   @Written    : 06/04/2019
   @Description: 38th batch farewell card
'''

import turtle

window = turtle.Screen()

def draw_shape(some_turtle, radius) :
        some_turtle.circle(radius, 60)
        some_turtle.left(120)
        some_turtle.circle(radius, 60)

def draw_flower():
    
    window.screensize(400, 350)
    window.bgcolor("#333")
    petal = turtle.Turtle()
    petal.shape("turtle")
    petal.color("#EC627C")
    petal.speed(10)
    petal.width(2)

    the_petals = 15
    the_radius = 150

    for _ in range(the_petals) :
        draw_shape(petal, the_radius)
        petal.left(360 / the_petals)


    stalk = turtle.Turtle()
    stalk.width(3)
    stalk.color("#EC627F")
    stalk.shape("turtle")
    stalk.right(90)
    stalk.forward(260)
    
draw_flower()

myPen = turtle.Turtle()
myPen.penup()
myPen.color("white")
myPen.goto(0, 280)
myPen.write("Farewell to CSE-38th Batch", False, "center", ("Gabriola", 34, ("bold","italic")))

myPen.goto(-10, 230)
myPen.write("May the blessing of Allah fill your future life with happiness and success", False, "center", ("Gabriola", 15))
myPen.penup()

myPen.goto(0, -330)
myPen.write("@Presented By: Md Mahedi Hasan", False, "center", ("Gabriola", 14, ("bold","italic")))

window.exitonclick()
