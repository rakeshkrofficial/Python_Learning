x=int(input("Enter x number:"))
y=int(input("Enter y number:"))
z=int(input("Enter z number:"))
n=int(input("Enter n number:"))

result=[]

for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k !=n:
                result.append([i,j,k])
print(result)