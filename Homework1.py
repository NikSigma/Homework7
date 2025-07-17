import turtle

turtle.bgcolor("black")

t = turtle.Turtle()
t.pensize(2)
t.speed(3)


t.color("red")
for _ in range(4):
    t.forward(100)
    t.left(90)


t.penup()
t.goto(150, 0)
t.pendown()

# Малюємо круг
t.color("green")
t.circle(50)


t.penup()
t.goto(-105, 0)
t.pendown()


t.color("blue")
for _ in range(6):
    t.forward(70)
    t.left(60)

turtle.done()
