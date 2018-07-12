n=input("Enter No: ")
d=[]
for i in range(2,n+1):
  if n%i==0:
    d.append(i)
d.sort()
print "Smallest Divisor: ",d[0]
