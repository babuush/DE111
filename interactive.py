import turtle
p1=turtle.Turtle()
sc=turtle.Screen()
p1.penup()
p1.speed(100)
def write_at_click(x,y):  	 
	p1.goto(x,y)
	p1.pendown()
	p1.circle(40)
	p1.penup()
    
sc.onclick(write_at_click)
sc.mainloop()
