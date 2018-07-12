def add(*arg):
    res = 0
    for i in arg:
        res+=i 
    return res
def pos_neg(num1):
    if num1<0:
        return "-ve"
    else:
        return "+ve"
def mul(a,b=2):
    return a*b
def get_res(branch,**subs):
    total=0
    for k,v in subs.items():
        if branch=="CSE" and k in ["c","java"]:
            total+=v
    return total

if __name__=="__main__":
    num=[]
    subs={"c":34,"java":36}
    for i in range(5):
        num.append(input("Enter No: "))
    res=add(*num)
    print "Addition of list ",res
    num1=input("Enter A No: ")
    print "No is: ",pos_neg(num1)
    print "Multiplication of ",num1," with default arg ",mul(num1)
    print "Multiplication of ",num1," without default arg ",mul(num1,4)
    print "score of java and c ",get_res("CSE",c=20,java=30,math=10)
    print "score of java and c ",get_res("CSE",**subs)
