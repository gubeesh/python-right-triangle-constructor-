import turtle
import math
x = abs(float(input("enter a number:")))
a=x
b=abs(x*x/4-1)
c=x*x/4+1 
turtle.forward(b)
turtle.left(90)
turtle.forward(a)
x = math.asin(b/c)*57.2958
turtle.left(180-x)
turtle.forward(c)
