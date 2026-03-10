#===================================================================================================================#
#       Take any digit of any length from user write a program to find the sum of all digit                         #
#===================================================================================================================#


num=input("Enter numbers:")
sum=0

for i in range(len(num)):
    sum=sum+int(num[i])
print("sum =",sum)


#===================================================================================================================#
#            Take input any number of any length from user write a program to find the sum of all number            #
#===================================================================================================================#

sum=0

while True:
    num=float(input("Enter number:"))

    if num==0:
        break
    sum =sum+num

print("Total sum =", sum)