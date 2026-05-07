import turtle as t
import random as r
from turtle_config import *

# Налаштування черепашки
t.shape(SHAPE)
t.pensize(PEN_SIZE)
t.color(COLOR)
t.fillcolor(FILL_COLOR)
t.speed(SPEED)

print_config()


# Завдання 1

t.penup()
t.goto(-250, 0)
t.pendown()

t.color("red")

for i in range(4):
    t.forward(80)
    t.right(90)

t.penup()
t.goto(0, 0)
t.pendown()

t.color("green")

for i in range(3):
    t.forward(80)
    t.left(120)

t.penup()
t.goto(250, 0)
t.pendown()

t.color("blue")

for i in range(5):
    t.forward(80)
    t.right(72)

# Завдання 2

t.penup()
t.goto(-100, -200)
t.pendown()

t.color("black")
t.fillcolor("yellow")

t.begin_fill()

for i in range(4):
    t.forward(150)
    t.left(90)

t.end_fill()

t.penup()
t.goto(-100, -50)
t.pendown()

t.color("black")
t.fillcolor("red")

t.begin_fill()

for i in range(3):
    t.forward(150)
    t.left(120)

t.end_fill()

# Завдання 3

t.penup()
t.goto(250, -150)
t.pendown()

t.speed(0)

for i in range(36):

    t.color(r.random(), r.random(), r.random())

    for j in range(4):
        t.forward(80)
        t.right(90)

    t.right(10)

t.done()