import turtle
turtle.Screen().bgcolor("orange")

num = int(turtle.Screen().numinput("Insert number", "Steps"))
length = int(turtle.Screen().numinput("Insert number", "Length of Steps"))
sk = turtle.Turtle()
for i in range(num):
   sk.fd(length)
   sk.rt(90)
   sk.fd(length)
   sk.lt(90)
sk.rt(180)
sk.fd(length*num)
sk.rt(90)
sk.fd(length*num)

turtle.done()


