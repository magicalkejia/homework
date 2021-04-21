# coding=utf-8
from Student import Student
from Teacher import Teacher
from Score import Class
import pandas


def CreateTeacher(number):
        for i in range(number):
            current = Teacher("firstname.txt","lastname.txt")
            print(current.tid,current.GetName())


if __name__ == "__main__":
    
    class1 = Class("Math","001",60)
    #print(class1.subject,class1.class_id,class1.class_num)
    class1.CreateStudent()
    class1.Exam("serious")
    #print(class1.score_detail)

   

  
