import turtle
p1=turtle.Turtle()
sc=turtle.Screen()
n = int(turtle.numinput('title', 'n'))
cx = int(turtle.numinput('title', 'cx'))
cy = int(turtle.numinput('title', 'cy'))
p1.color('blue')
p1.speed(100)
p1.penup()  
side = 50 
p1.goto(cx,cy)
p1.pendown()
p1.dot(10, 'green')
p1.penup()
for i in range(1,n):
	p1.goto(cx-15-10*i,cy-15-10*i)
	p1.pendown()
	for j in range(4):
		p1.fd(side)
		p1.lt(90)
	p1.penup() 
	side += 20

p1.penup()

sc.mainloop()
