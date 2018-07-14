start=input("Enter Start: ")
end=input("Enter end: ")
print "Number which are divisible by 7 and multiple of 5 in range ",start," ",end," = ",
for i in range(start,end+1):
    if i%7 == 0 and i%5 == 0:
         print i,
