#===================================================================================================================#
#                                  1.Guessing Number                                                                #
#===================================================================================================================#


import random
win_num=random.randint(1,10)
n=int(input("Enter guess number:"))
while True:
    if win_num==n:
        print("You won !")
        break
    
    else:

        if win_num >n:
            print("You guess number is low !")

        else:
            print("You guess number is high!")
        n=int(input("Enter guess number:"))
