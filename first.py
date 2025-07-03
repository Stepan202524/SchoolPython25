# Черепашья графика
import turtle # as t - Сократим до t, чтобы не писать turtle

turtle.speed(9)
turtle.penup()
turtle.goto(-100, -200)
turtle.pendown()

def tree(leng):
    if leng < 10:
        return
    turtle.forward(leng)
    turtle.left(30)
    tree(leng * 0.7)
    turtle.right(60)
    tree(leng * 0.7)
    turtle.left(30)
    turtle.backward(leng)

turtle.left(90)
tree(100)


N = 5
colors = ['red', 'green', 'blue', 'orange', 'yellow']

turtle.bgcolor('black')
angle = 360 // len(colors) - 1

for x in range(100):
    turtle.pencolor(colors[x % len(colors)])
    turtle.width(x // 100 + 1)
    turtle.forward(x)
    turtle.left(angle)


def square(side):
    for _ in range(5):
        turtle.forward(side)
        turtle.left(360 // N)

def circle(radius):
    for _ in range(5):
        turtle.circle(radius)
        turtle.right(360 // N)

circle(60)

for _ in range(N):
    square(40)
    turtle.left(360 // 5)

turtle.mainloop()