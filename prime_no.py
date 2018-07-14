def prime(num):
    for i in range(2,num/2+1):
        if num%i == 0:
            return "It is Not a Prime No: "
            break
    else:
        return "It is a Prime No: "
n=input("Enter No: ")
print prime(n)
