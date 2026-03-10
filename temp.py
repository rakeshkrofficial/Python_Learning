# while True:
#     num1 = float(input("Enter first number: "))
#     op = input("Enter operator (+, -, *, /) or q to quit: ")

#     if op == 'q':
#         print("Calculator बंद हो गया")
#         break

#     num2 = float(input("Enter second number: "))

#     if op == '+':
#         result = num1 + num2
#     elif op == '-':
#         result = num1 - num2
#     elif op == '*':
#         result = num1 * num2
#     elif op == '/':
#         if num2 == 0:
#             print("❌ Division by zero not allowed")
#             continue
#         result = num1 / num2
#     else:
#         print("❌ Invalid operator")
#         continue

#     print("Result =", result)


result = float(input("Enter first number: "))

while True:
    op = input("Enter operator (+, -, *, /) or = to finish: ")

    if op == '=':
        break

    num = float(input("Enter next number: "))

    if op == '+':
        result = result + num
    elif op == '-':
        result = result - num
    elif op == '*':
        result = result * num
    elif op == '/':
        if num == 0:
            print("❌ Division by zero not allowed")
            continue
        result = result / num
    else:
        print("❌ Invalid operator")

print("✅ Final Result =", result)