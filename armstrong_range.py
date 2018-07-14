start=input("\nEnter start: ")
end=input("Enter end: ")
print "Armstrong Number in range ",start," ",end
for i in range(start,end+1):
    total=0
    temp=i
    while temp > 0:
        digit = temp % 10
        total += digit ** 3
        temp //= 10
    if i == total:
        print i,
   
