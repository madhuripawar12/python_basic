a=[]
c=[]
n1=input("Enter number of elements:")
for i in range(1,n1+1):
    b=input("Enter element:")
    a.append(b)
n2=input("Enter number of elements:")
for i in range(1,n2+1):
    d=input("Enter element:")
    c.append(d)
new=a+c
new.sort()
print "Sorted list is:",new 
