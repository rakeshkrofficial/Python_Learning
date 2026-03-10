import random

computer_num=random.randint(1,100)

user_num=int(input("Enter Any number:"))
sum=user_num + computer_num

if sum %2==0:
    print("You won!")
else:
    print("You lose!")