n=input("Enter No: ")
count=0
while n>0:
  rem=n%10
  count+=1
  n=n//10
print "Number of digit: ",count
