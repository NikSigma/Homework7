import turtle
import time

t = turtle.Turtle()
t.hideturtle()
t.penup()
t.goto(-50, -50)
t.pendown()


t.begin_fill()
t.fillcolor("green")
for _ in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()


screen = turtle.Screen()
colors = ["green", "yellow", "red"]

while True:
    for color in colors:
        t.fillcolor(color)
        t.begin_fill()
        for _ in range(4):
            t.forward(100)
            t.left(90)
        t.end_fill()
        time.sleep(0.5)
