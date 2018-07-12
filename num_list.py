n=input("Enter no: ")
a=[]
for i in range(1,n+1):
    print i,
    if i<n:
        print "+",
    a.append(i)
print "=",sum(a)


