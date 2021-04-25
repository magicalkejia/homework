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
    
    
    class1 = Class("001",60)
    #print(class1.subject,class1.class_id,class1.class_num)
    class1.CreateStudent()

    #delattr(class1,'score_record')
    class1.Exam("serious","初一",class1.score_record)
    print("End")


    

    #class1.Excel()
    #print(class1.score_detail)

   

  
