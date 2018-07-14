def prime(num):
    for i in range(2,num/2+1):
        if num%i == 0:
            return 0
            break
    else:
        return 1

n=input("Enter Number: ")
for i in range(2,n/2):
    if n%i==0:
        if prime(i)==1:
             print i
        
