import turtle
sk = turtle.Turtle()
# sk.shape("turtle")
# num = int(turtle.Screen().numinput("Insert number", "Steps"))
x = 20
sk.speed(2)
for i in range(5):
    x+=20
    for j in range(5):
        sk.fd(x)
        sk.lt(90)
turtle.done()
