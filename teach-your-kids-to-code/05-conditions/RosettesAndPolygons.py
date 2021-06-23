import turtle

t = turtle.Pen()

# Ask the user for the number of sides, default to
sides = int(turtle.numinput("Number of sides", "How many sides in your spiral?", 4))

# Our outer spiral loop for polygons and rosettes, rom size 5 to 75
for m in range(5, 75):
    t.left(360/sides + 5)
    t.width(m//25 + 1)
    t.penup()
    t.forward(m*4)  # Move to next corner
    t.pendown()

    if (m % 2 == 0):
        for n in range(sides):
            t.circle(m/3)
            t.right(360/sides)
    else:
        for n in range(sides):
            t.forward(m)
            t.right(360/sides)
