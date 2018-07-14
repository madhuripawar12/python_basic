num =input("Enter the Range Number: ")
i = 0
fno = 0
prev= 1
           
for i in range(num):
    if(i <= 1):
        fib = i
    else:
        fib = fno + prev
        fno = prev
        prev = fib
    print fib,

