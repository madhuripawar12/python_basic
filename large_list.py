a=[]
n=input("Enter number of elements:")
for i in range(1,n+1):
    b=input("Enter element:")
    a.append(b)
a.sort()
print("Largest element is:",a[n-1])
