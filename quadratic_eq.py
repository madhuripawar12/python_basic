import cmath
def eq(a,b,c):
    d=4*a*c
    e=b*b
    f=2*a
    r1=-b+cmath.sqrt(e-d)/f
    r2=-b-cmath.sqrt(e-d)/f
    return r1,r2
a=input("Enter Value Of a: ")
b=input("Enter Value Of b: ")
c=input("Enter Value Of c: ")
print "Solution of Quadratic Equation is: ",eq(a,b,c)
