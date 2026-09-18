PI = 3.14

def cube(side):
    valume = side*side*side

    print("Cube valume is: ",valume)

def sphera(radius):

    valume = 4*PI*radius*radius*radius/3

    print("Sphera valume is: ",valume)

def cylinder(radius,height):

    valume = PI*radius*radius*height

    print("Cylinder valume is: ",valume)

while True:


    user_input = input("""Hey, What you want to find valume !
    1.Enter 1 to cube valume
    2.Enter 2 to sphera valume
    3.Enter 3 to cylinder valume
    4.Enter 4 to exit: """)


    if(user_input == '1'):
        side = float(input("Enter value of side: "))
        print("\n")
        cube(side)
        print("\n")

    elif(user_input == '2'):
        radius = float(input("Enter value of radius: "))

        print("\n")
        sphera(radius)
        print("\n")

    elif(user_input == '3'):
        radius = float(input("Enter value of radius: "))

        height = float(input("Enter value of height: "))

        print("\n")
        cylinder(radius,height)
        print("\n")

    elif(user_input == '4'):
        print("Thank you !")
        break

    else:
        print("Invalid input !")
