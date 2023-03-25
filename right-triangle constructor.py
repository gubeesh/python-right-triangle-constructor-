import turtle
import math
x = abs(float(input("enter a number:")))
y = input("should the constructed right-triangle be isoceles?(y if yes, leave if no)?: ")


if y == "y":
    turtle.forward(x)
    turtle.left(135)
    turtle.forward(math.sqrt(2)*x)
    turtle.left(135)
    turtle.forward(x)

else:
    a=x
    b=abs(x*x/4-1)
    c=x*x/4+1 
    turtle.forward(b)
    turtle.left(90)
    turtle.forward(a)
    x = math.asin(b/c)*57.2958
    turtle.left(180-x)
    turtle.forward(c)
