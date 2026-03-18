num=int(input("Enter a number:"))

sum_digits=0

while num > 0:
    sum_digits=num % 10 + sum_digits

    num = num// 10

print("Sum of Digit =",sum_digits)