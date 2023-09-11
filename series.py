import turtle
y=0
sk=turtle.Turtle()
for x in range(1,12):
	y=20*(x-1)
	sk.penup()
	sk.goto(0,20*x)
	sk.write(y)
	sk.pendown()
turtle.done()
