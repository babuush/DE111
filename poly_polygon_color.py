import turtle
sk=turtle.Turtle()
sk.speed(50)
sk.pensize(3)
side = 4
size = int(turtle.numinput('title', 'Polygon size'))
color = ["brown", "green", "red"]
for i in range(3):
		sk.pencolor(color[i])	
		for j in range(side):
			sk.fd(size)
			sk.lt(360/side)
		side += 1
turtle.done()
