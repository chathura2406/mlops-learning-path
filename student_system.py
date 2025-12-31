class Student: 
    def __init__(self, name , age,marks ):
        self.name = name
        self.age =age
        self.marks = marks


    def get_grade (self):
        if self.marks >= 80:
            print(f"{self.name} has received an A Grade ")
        elif self .marks >= 60:
            print (f"{self.name} has received teh B Pass")
        else :
            print ("cant determined the grade")


student1 =Student ("sadun ", 19, 85 )
student2 =Student ("kumar",20,67)


student1.get_grade ()
student2.get_grade ()


