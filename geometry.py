PI = 3.14

def circle(radius):
    area = PI * radius

    print("")
    print("Area of circle: ",area)
    print("")

def rectangle(length,breadth):

    area = length * breadth

    print("")
    print("Area of rectangle: ",area)
    print("")

def triangle(base,height):

    area = base*height/2

    print("")
    print("Area of triangle: ",area)
    print("")

while True:

    user_input = input("""Hey, What you want !
    1. Enter 1 to Area of circle
    2. Enter 2 to Area of rectangle
    3. Enter 3 to Area of triangle
    4. Enter 4 to exit: """)

    if(user_input == '1'):

        radius = float(input("Enter radius of circle: "))

        circle(radius)

    elif(user_input == '2'):

        length = float(input("Enter length of rectangle: "))
        breadth = float(input("Enter breadth of rectangle: "))

        rectangle(length,breadth)

    elif(user_input == '3'):

        base = float(input("Enter base of triangle: "))
        height = float(input("Enter height of triangle: "))

        triangle(base,height)

    elif(user_input == '4'):

        print("Thank you !")
        break

    else:

        print("Invalid input !")
