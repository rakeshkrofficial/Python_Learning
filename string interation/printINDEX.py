# method 1

x="Welocome to my python code"
for a in range(len(x)):
    print(x[a])

 # method 2
b="my dear sir"
for a in b:
    print(a)

print("")

# print to reverse side

# method 1

y=x[-1::-1]
for i in range(len(y)):
    print(y[i])

# method 2
t=len(x)
for i in range(t-1,-1,-1):
    print(x[i])