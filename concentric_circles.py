import turtle
p1=turtle.Turtle()
sc=turtle.Screen()
p1.speed(200)
p1.penup() 
def write_at_click(x,y):      
	p1.goto(x,y)
	p1.pendown()
	p1.dot(10, 'green')
	p1.penup()
	p1.goto(x,y-40)
	p1.pendown()
	p1.circle(40)
	p1.penup()    
sc.onclick(write_at_click)
sc.mainloop()