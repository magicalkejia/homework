# coding=utf-8
from Student import Student
from Teacher import Teacher
from Score import Class
import pandas


def CreateTeacher(number):
        for i in range(number):
            current = Teacher("firstname.txt","lastname.txt")
            print(current.tid,current.GetName())

def init():
    Id = input("Input the id of your class")
    number = input("Input the amnout of your class ")
    attri = input("Input the attitude of class teacher")
    period = input("Input the grade of your class,it must be chinese character '初一/初二/初三/中考', any other input will cause error!!!")


if __name__ == "__main__":


    
    subject_bonus = {"语文":(1,0.3,-0.1),"数学":(1,0.3,-0.1),"英语":(1,0.3,-0.1),"地理":(0.3,0.1,-0.1),"历史":(0.3,0.1,-0.1),"政治":(0.3,0.1,-0.1),"体育":(0.3,0.1,-0.1),"音乐":(0.3,0.1,-0.1),"画画":(0.3,0.1,-0.1),"物理":(0.3,0.1,-0.1),"化学":(0.3,0.1,-0.1)}
    class1 = Class("001",60)
    class1.CreateStudent()

    class1.Exam("serious","初一")
    #print(class1.score_record["初一"])
    class1.Excel("初一")
    class1.Exam("casual","初二")
    class1.Excel("初二")
    print("End")


   

  
