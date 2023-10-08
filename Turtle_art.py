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
tom.pensize(15)

for i in range(200):
    tom.speed(0)
    tom.color(random_color())
    tom.forward(30)
    tom.setheading(choice(motion))











screen = Screen()
screen.exitonclick()