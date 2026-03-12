n1,n2=map(int,input("Enter number of elements in list1 and list2:").split())
L1=[]
L2=[]
L3=[]

for i in range(n1):
    L1.append(eval(input("Enter element of list1 :")))

for i in range(n2):
    L2.append(eval(input("Enter element of list2 :")))

print(L1)
print(L2)

for i in L1:

    if i in L2:
        L3.append(i)

print(L3)