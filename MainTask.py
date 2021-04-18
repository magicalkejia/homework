# coding=utf-8
from Student import Student
from Teacher import Teacher
from Score import ClassScore
import pandas
def CreateStudent(number):
        for i in range(number):
            current = Student(2021,"firstname.txt","lastname.txt")
            print(current.sid,current.GetName())

def CreateTeacher(number):
        for i in range(number):
            current = Teacher("firstname.txt","lastname.txt")
            print(current.tid,current.GetName())


if __name__ == "__main__":
    
    class1 = ClassScore("Math","001",60)
    print(class1.subject,class1.class_id,class1.class_num)
    class1.Exam("serious")
    print(class1.score_detail)

   

  
