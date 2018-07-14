n=input("Enter the number of elements to be in the list: ")
l=[]
for i in range(0,n):
    a=input("Element: ")
    l.append(a)
even=0
odd=0
neg=0
for j in l:
    if(j>0):
        if(j%2==0):
            even+=j
        else:
            odd+=j
    else:
        neg+=j
print "Sum of all positive even numbers:",even
print "Sum of all positive odd numbers:",odd
print "Sum of all negative numbers:",neg
