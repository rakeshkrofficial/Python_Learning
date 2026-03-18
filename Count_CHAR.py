name=input("Enter name:")
char=input("Enter any charcter:")
length=len(name.replace(" ",""))

print("length (Excluding space):",length)

count=name.lower().count(char.lower())

print("Count of Charecters :",count)