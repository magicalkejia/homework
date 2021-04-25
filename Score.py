import random
from Student import Student
import pandas as pd
import xlsxwriter
# coding=utf-8

class Class():
    score_record = {}
    seven = {}
    eight = {}
    nine = {}
    end = {}
    def __init__(self,class_id,class_num):
      
        self.class_id = class_id
        self.class_num = class_num
        self.Student = []
        self.score_detail = []
        self.offset_up = 5
        self.offset_down = 5
        self.subject_list = ["语文","数学","英语","地理","生物","历史","政治","体育","音乐","画画","物理","化学"]
        self.seventh = ["期中","期末","期中（2）","期末（2）"]
        self.eighth = ["期中","期末","期中（2）","期末（2）"]
        self.nineth = ["第一次月考","第二次月考","期中考试","第三次月考","第四次月考","期末考试","第一次月考（2）","第二次月考（2）","期中考试（2）","第三次月考（2）","第四次月考（2）","期末考试（2）"}
        self.end  = ["中考"]


    
    def CreateStudent(self):
        for i in range(self.class_num):

            current = Student(2021,"firstname.txt","lastname.txt")
            current.GetName()
            tup = (current.sid,current.stdname)

            self.Student.append(tup)
        

    
    def Exam_offset(self,offset,up_number,down_number):

        up_number = int(up_number)
        down_number = int(down_number)
        if(offset == True):
            for i in range(self.class_num):
                    
                    if (up_number> 0):
                        self.score_detail[i] += random.randint(1,self.offset_up)
                           
                        up_number -= 1
                    if((i>up_number) & (down_number>0)):
                        self.score_detail[i] += random.randint(1,self.offset_down)
                                        
                        down_number -= 1
             
                    
        else:
            
            
            def rmdata(self):
                temp = []
                for i in range(self.class_num):
                    num = random.randint(0,95)
                    temp.append(num)               
                self.score_detail = temp
                del temp                   

    
            rmdata(self)


    def ScoreStata(self,data):
        origin = data
        order = list(data)
        index = []
        for i in range(len(order)-1):
            maxindex = i
            for j in range(i+1,len(order)):
                if order[j] > order[maxindex]:
                    maxindex = j
                if i != maxindex:
                    order[i], order[maxindex] = order[maxindex],order[i]

      
        for i in range(len(origin)):
            for j in range(len(order)):
                if origin[i] == order[j]:
                    index.append(j)
        
        return index
     
        


    def CheckOffset(self,before,after):
        summary = 0
        #ls = []
        for i in range(len(after)):
            change = abs(after[i] - before[i])
            summary += change
        if summary <=300:
            return True
        else:
            return False
        
 
    def Exam(self,teacher_attr,time,score_record):


        def Package(self,score_record,length):
            temp = []
           
            for i in range (length):
                self.Exam_offset(False,up_number,down_number)
            
                self.Exam_offset(True,up_number,down_number)

                temp.append(self.score_detail)
                package = tuple(temp)
                self.score_detail = []
            return package
        #处理老师工作态度参数
        if teacher_attr == "serious":
            up_number = 0.05*self.class_num
            down_number = 0.03*self.class_num
            

        elif teacher_attr == "casual":
            up_number = 0.05*self.class_num
            down_number = 0.03*self.class_num
         
     
        else:
            print("unkonwn attribute of teacher,please input serious/casual")

        #处理时间参数
        if time =="初一"：
            Excute(self,score_record,len(self.subject_list)-2)
            for name in self.seventh:
                seven['']

        elif time == "初二":
            Excute(self,score_record,len(self.subject_list)-1)
        elif time == "初三":
            Excute(self,score_record,len(self.subject_list))
        else:
            print("unkonwn period ,please input '初一/初二/初三'")
    
    def Bonus(self):
        subject_bonus = {"语文":(1,0.3,-0.1),"数学":(1,0.3,-0.1),"英语":(1,0.3,-0.1),"地理":(0.3,0.1,-0.1),"历史":(0.3,0.1,-0.1),"政治":(0.3,0.1,-0.1),"体育":(0.3,0.1,-0.1),"音乐":(0.3,0.1,-0.1),"画画":(0.3,0.1,-0.1),"物理":(0.3,0.1,-0.1),"化学":(0.3,0.1,-0.1)}




    def Excel(self):

        ls1 = []
        ls2 = []
        for tup in self.Student:

            ls1.append(tup[0])
            ls2.append(tup[1])

        # Create a Pandas dataframe from some data.
        Data = pd.DataFrame({'学号': ls1,'名字': ls2,'语文': self.score_record[0],"数学":self.score_record[1]})
       
   
        writer = pd.ExcelWriter('ClassScore.xlsx', engine='xlsxwriter')

        # Convert the dataframe to an XlsxWriter Excel object.
        Data.to_excel(writer,sheet_name='{0}班级{1}成绩'.format(self.class_id,"期中"),startcol=0, index=False)
 

        # Close the Pandas Excel writer and output the Excel file.
        writer.save()

        

    




