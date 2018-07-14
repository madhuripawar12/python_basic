import math
a=input("Enter first side: ")
b=input("Enter second side: ")
c=input("Enter third side: ")
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print "Area of the triangle is: ",round(area,2)
