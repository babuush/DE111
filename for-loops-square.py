import turtle
p1=turtle.Turtle()
p1.speed(50)
color_list = ['red', 'blue', 'green', 'orange']
side_list = [50, 100, 150, 200]
for i in range(len(color_list)):
    p1.color(color_list[i])
    side = side_list[i]
    for _ in range(4):
        p1.fd(side)
        p1.rt(90)
turtle.done()
