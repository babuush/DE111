import turtle
from math import pi
sk=turtle.Turtle()
sk.speed(50)
sk.pensize(3)

side = 3
radius = int(turtle.numinput('title', 'Radius Lenght'))
size = int(turtle.numinput('title', 'Polygon size'))
# color = ["brown", "green", "red"]
for i in range(3):
		# sk.pencolor(color[i])	
		for j in range(side):
			x = rad*cos(theta)
			turtle.goto(x, y=None)
		side += 3
turtle.done()
