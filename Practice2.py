#create class student that takes 3 marks and has     a method average().

class student:

    def __init__(self,name,list_of_mark):
        self.name=name
        self.list_of_mark=list_of_mark

    def average(self):

        sum = 0
        for eachValue in self.list_of_mark:
            sum = sum + eachValue
        average = sum/3
        print("Average is :", average)

student1=student("aditya",[68,87,74])
student1.average()
