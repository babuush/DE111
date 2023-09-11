import turtle
turtle.Screen().bgcolor("orange")
num = int(turtle.Screen().numinput("Insert number", "Steps"))
length = int(turtle.Screen().numinput("Insert number", "Length of Steps"))
turtle.shape("turtle")


for i in range(num):
   turtle.fd(length)
   turtle.rt(90)
   turtle.fd(length)
   turtle.lt(90)
turtle.rt(180)
turtle.fd(length*num)
turtle.rt(90)
turtle.fd(length*num)

turtle.done()


