list=[]
sum=0
for i in range(7):
    num=input("Input No: ")
    list.append(num)
for i in list:
    sum+=i
print "Average Of List := ",sum/len(list)
