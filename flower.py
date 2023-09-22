from turtle import *
import colorsys
import math

speed(0)
bgcolor("black")


#Stem
penup()
goto(50, -280)
pendown()
setheading(90)
fillcolor("#648e00") 
begin_fill()
forward(200)
left(90)
forward(20)
left(90)
forward(200)
end_fill()


#Petals
goto(0, -40)
h = 0

for i in range(16):
    for j in range(18):
        c= colorsys.hsv_to_rgb(0.125 , 1, 1)
        color(c)
        rt(90)
        circle(150-j*6, 90)
        lt(90)
        circle(150-j*6, 90)
        rt(180)
    circle(40, 24)

#Center Flower
color("black") 
shape("turtle")
fillcolor("#804000")
phi = 137.508 * (math.pi/ 180.0)
for i in range (200):
    r = 4 * math.sqrt(i)
    theta = i*phi
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    penup()
    goto(x+40, y-40)
    setheading(i * 137.508)
    pendown()
    stamp()

#title
penup()
color("#b11226")
goto(-200,100)  
write("Te Amo\n  Babe", align="center", font=("Arial", 24, "bold"))
hideturtle()
done()


