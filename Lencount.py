name = input("Enter your name: ")
ch = input("Enter a character: ")

# Length of name excluding spaces
length = len(name.replace(" ", ""))

# Count of character (case sensitive)
count = name.count(ch)

print("Length of name (excluding spaces):", length)
print("Count of character:", count)
