#===================================================================================================================#
#                                                                                                 #
#===================================================================================================================#

import random
choices=["rock","paper","scissors"]
computer_choices=random.choice(choices)

user_choices=input("Enter (rock,paper,scissors or quit for end):")

while True:
    if user_choices=='quit':
        print("Game is End")
        break


    if user_choices not in choices:

        print("invalid choices")
        user_choices=input("Enter (rock/paper/scissors):")

    

    if(user_choices=='paper' and computer_choices=='rock') or (user_choices=='scissors' and computer_choices=='paper') or (user_choices=='rock'and computer_choices=='scissors'):
        print("User won! \nCONGRATUALTION !!!")
        break

    else:
        if user_choices==computer_choices:
            print("Match Drow")
        else:
            print("Computer won **")
        break
    



# import random
# choices=["rock","paper","scissors"]

# user_choices=input("Enter (rock/paper/scissors)")

# while True:
#     if user_choices=='quit':
#         print("Game is end...")
#         break

#     if user_choices not in choices:
#         print("invalid choices")
#         continue

#     computer_choices=random.choice(choices)

#     if(user_choices=='paper' and computer_choices=='rock') or (user_choices=='scissors' and computer_choices=='paper') or (user_choices=='rock'and computer_choices=='scissors'):
#         print("User won! \nCONGRATUALTION !!!")
#         break

#     else:
#         if user_choices==computer_choices:
#             print("Match Drow")
#         else:
#             print("Computer won **")
#         break