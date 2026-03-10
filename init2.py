class student:
    schoolName="Shobhit university meerut"

    def __init__(self,name,course,roll_num):  #method
       # print("Whenever a new object is create i am called automaticaly")

        self.name=name
        self.course=course
        self.roll_num=roll_num


student1= student("Rakesh","BCA","132") #init method will be called
print("student name -",student1.name)
print("student course->",student1.course)
print("student roll number =",student1.roll_num,"\n")

student2= student("kumar","b.sc","321")
print("student name ->",student2.name)
print("student course ->",student2.course)
print("student roll number =",student2.roll_num,"\n")