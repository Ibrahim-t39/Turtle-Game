from random import *
from turtle import Screen
import turtle as t

tom = t.Turtle()
t.colormode(255)

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)

motion = [0, 90, 180, 270]
tom.shape("turtle")
tom.color("blue")

tom.speed(0)
gap_size=0
while gap_size <= 360:
    tom.color(random_color())
    tom.seth(gap_size)
    tom.circle(100)
    gap_size += 7.4
    











screen = Screen()
screen.exitonclick()