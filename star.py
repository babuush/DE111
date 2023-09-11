import turtle
t = turtle.Turtle()
t.speed(1)
t.color('red')
s=25
n=15
degree=360/n
t.width(3)
for x in range(n):
	t.fd(s)
	t.bk(s)
	t.rt(degree)
turtle.done()
