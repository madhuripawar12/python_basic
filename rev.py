n=input("Enter No: ")
rev=0
print "Original Number: ",n
while n>0 :
    d=n%10
    rev=rev*10+d
    n=n//10

print "Reverse of the number: ",rev
