import turtle

t = turtle.Pen()
turtle.bgcolor("black")

# Set up a list of any 8 valid Python color names
colors = ["red", "yellow", "blue", "green", "orange", "purple", "white", "gray"]

sides = int(turtle.numinput("Number of sides", "How many sides do you want (1-8)?", 4, 1, 8))
your_name = turtle.textinput("Enter your name", "What is your name?")

for x in range(360):
    t.pencolor(colors[x % sides])
    t.penup()
    t.forward(x * 3 / sides + x)
    t.pendown()
    t.write(your_name, font = ("Arial", int( (x + 4) / 4), "bold"))
    t.left(360 / sides + 1)
    t.width(x * sides / 200)
