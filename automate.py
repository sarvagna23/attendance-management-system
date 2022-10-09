import turtle
import colorsys
t=turtle.Turtle()
s=turtle.Screen()
t.speed(1000)
n=150
h=0

t.left(100)
for i in range(360):
    c=colorsys.hsv_to_rgb(h,1,0.8)
    h+= 1/n
    t.color(c)
    t.left(144)
    t.forward(i*5)
