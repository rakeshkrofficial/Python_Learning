result=0

while True:
    num1=float(input("Enter  number:"))
    op=input("Enter opertor(+,-,*,/) or q for quit:")
    
    if op=='q':
        print("calculator closed")
        break

    num2=float(input("Enter number:"))
    
    if op=='+' :
        result=num1+num2
    elif op=='-':
        result=num1-num2
    elif op=='*':
        result=num1*num2
    elif op=='/':
        if num2!=0:
            div=num1/num2
        else:
            print("cannot divide by zero")
            continue
    else:
        print("invalid operator")
        continue
print("Result=",result)
            

    