from turtle import *


#drawing a square 

width(10)
speed(30)

color("green")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(50)
left(90) 

#end of square

#door 

color("purple")
begin_fill()
forward(100)
right(90)

forward(70)
right(90)

forward(100)
left(90)
end_fill()

#end of door

#roof
penup()
goto(200, 200)
pendown()
color("yellow")
begin_fill()
left(120)
forward(200)

left(120)
forward(200)
end_fill()

#end of roof 

#start of door handle

penup()
goto(50, 50)
pendown()
color("red")
left(120)
forward(10)

 #end of door handle

#start of left window

color("brown")
penup()

goto(60,110)

width(3)

pendown()

left(90)
forward(70)

left(90)
forward(50)

left(90)
forward(70)

left(90)
forward(50)

left(90)
forward(35)

left(90)
forward(50)

left(90)
forward(35)

left(90)
forward(25)

left(90)
forward(70)

#end of left window

#start of right window

penup()

goto(180,110)

pendown()

forward(70)

left(90)
forward(50)

left(90)
forward(70)

left(90)
forward(50)

left(90)
forward(35)

left(90)
forward(50)

left(90)
forward(35)

left(90)
forward(25)

left(90)
forward(70)

#end of right window

penup()

left(90)
forward(300)











     



exitonclick()
