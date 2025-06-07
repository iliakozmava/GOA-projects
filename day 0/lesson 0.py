from turtle import *


#we want to paint a house

#step 1: draw a square
speed(30)
width("7")
color("purple")
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

#drawing a door
forward(70)
color("yellow")
begin_fill()
left(90)
forward(100)
right(90)
forward(60)
right(90)
forward(100)
end_fill()


penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(70, 110,)
pendown()

color("brown")
right(60)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(25)
right(90)
forward(50)
right(180)
forward(25)
right(90)
forward(25)
right(180)
forward(50)

penup()
goto(130, 110)
pendown()

forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(25)
left(90)
forward(50)
left(180)
forward(25)
left(90)
forward(25)
left(180)
forward(50)

exitonclick()