import turtle
import math
x = float(input("enter a number:"))
#
a=2x
b=x*x-1  
c=x*x+1 
turtle.forward(b)
turtle.right(90)
turtle.forward(a)
#the function math.asin returns the values in radians, where in 1 radian = 57.2958 degrees
x = math.asin(b/c)*57.2958
turtle.right(180-x)
turtle.forward(c)
