class student:
    schoolName="Shobhit university meerut"

    def __init__(self):
        print("Whenever a new object is create i am called automaticaly")
        print(self)

student1= student() #init method will be called
print("student 1 = ", student1.schoolName)

student2= student()
print("my college name is",student2.schoolName)