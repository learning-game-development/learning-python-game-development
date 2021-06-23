import turtle

turtle.bgcolor("black")
colors = ["red", "yellow", "blue", "green"]

t = turtle.Pen()
for x in range(100):
    t.pencolor(colors[x % 4])
    t.circle(x)
    t.left(91)
