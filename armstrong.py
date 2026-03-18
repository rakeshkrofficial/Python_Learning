num=int(input("Enter a number:"))

num1=num
l=len(str(num))
temp=0

for i in range(l):
    temp=(num%10)**l+temp

    num=num//10

if temp==num1:
    print(num1," is Armstrong")

else:
    print(num1 ," is not Armstrong")

