a=[]
n=input("Enter the number of elements in list:")
for x in range(0,n):
    element=input("Enter element" + str(x+1) + ":")
    a.append(element)
temp=a[0]
a[0]=a[n-1]
a[n-1]=temp
print "New list is: ",a 
