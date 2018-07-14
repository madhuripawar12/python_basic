def prime(num):
    for i in range(2,num/2):
        if num%i == 0:
            return ""
            break
    else:
        return num,
a=input("Enter start: ")
b=input("Enter end: ")
for j in range(a,b):
    print prime(j)
