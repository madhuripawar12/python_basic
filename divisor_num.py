n=input("Enter No: ")
print "Divisor of No ",n," = ",
for i in range(2,n/2+1):
    if n%i == 0:
        print i,
