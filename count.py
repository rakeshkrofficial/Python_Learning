#===================================================================================================================#
#                                 this is beginner level method !                                                   #
#===================================================================================================================#


# word="Artificial"
# count=0

# for ch in word:
#     if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
#         count +=1
# print("number of vowel is =", count)


#===================================================================================================================#
#                                                best method                                                        #
#===================================================================================================================#

str=input("Enter any String:")

x=str.lower()

vowel=0
consonent=0

for i in range(len(x)):
    if x[i]=='a' or x[i]=='e' or x[i]=='i' or x[i]=='o' or x[i]=='u':

         vowel=vowel+1

    else:
        consonent=consonent+1

print("vowel count is",vowel,"consonent count is",consonent)