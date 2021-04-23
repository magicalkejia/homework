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
    subject = {"语文":True,"数学":True,"英语":True,"地理":True,"历史":True,"政治":True,"体育":True,"音乐":True,"画画":True,"物理":True,"化学":True}
    
    class1 = Class("001",60)
    #print(class1.subject,class1.class_id,class1.class_num)
    class1.CreateStudent()
    class1.Exam("serious",subject)
    class1.Excel()
    #print(class1.score_detail)

   

  
