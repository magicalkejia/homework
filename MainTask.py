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


    
    class1 = Class("001",60)
    class1.CreateStudent()
    class1.Exam("casual","初一")
    class1.Bonus(subject_bonus)


    print("End")


   

  
