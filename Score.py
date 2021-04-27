import random
from Student import Student
from Teacher import Teacher
import pandas as pd
import xlsxwriter
import matplotlib.pyplot as plt
import numpy as np
# coding=utf-8

class Class():

    def __init__(self,class_id,class_num):
      
        self.class_id = class_id
        self.class_num = class_num
        self.Student = []
        self.teacher_list = []
        self.teacher_id = []
        self.score_detail = []
        self.offset_up = 5
        self.offset_down = 5
        self.subject_list = ["语文","数学","英语","地理","生物","历史","政治","体育","音乐","画画","物理","化学"]
        self.seventh = ["期中考试","期末考试","期中考试（2）","期末考试（2）"]
        self.eighth = ["期中考试","期末考试","期中考试（2）","期末考试（2）"]
        self.nineth = ["第一次月考","第二次月考","期中考试","第三次月考","第四次月考","期末考试","第一次月考（2）","第二次月考（2）","期中考试（2）","第三次月考（2）","第四次月考（2）","期末考试（2）"]
        self.end_key  = ["中考"]
        #以上self 主要充作字典的键
        #以下self作为空字典存储实际结果
        self.score_record = {}
        self.seven = {}
        self.eight = {}
        self.nine = {}
        self.end = {}
        self.workload = {"语文":0 ,"数学":0,"英语":0,"地理":0,"生物":0,"历史":0,"政治":0,"体育":0,"音乐":0,"画画":0,"物理":0,"化学":0}


    
    def CreateStudent(self):
        for i in range(self.class_num):

            current = Student(2021,"firstname.txt","lastname.txt")
            current.GetName()
            tup = (current.sid,current.stdname)

            self.Student.append(tup)
        
    def CreateTeacher(self):
        ls = []
        ls2 = []
        self.teacher_num = len(self.subject_list)
        for i in range(self.teacher_num):
            current = Teacher("firstname.txt","lastname.txt")
            Name = current.GetName()
            Id = current.tid
            ls.append(Name)
            ls2.append(Id)
        self.teacher_list = ls
        self.teacher_id = ls2
        #self.teacher_list = self.teacher_list
        #elf.teacher_id = self.teacher_id

        del ls
        del ls2 



    
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




        
 
    def Exam(self,teacher_attr,time):

        #处理老师工作态度参数
        if teacher_attr == "serious":
            up_number = 0.05*self.class_num
            down_number = 0.03*self.class_num
            

        elif teacher_attr == "casual":
            up_number = 0.05*self.class_num
            down_number = 0.03*self.class_num
         
     
        else:
            print("unkonwn attribute of teacher,please input serious/casual")
        
        def Bonus(self,score_detail,subject):

            subject_bonus = {"语文":(1,0.3,-0.1),"数学":(1,0.3,-0.1),"英语":(1,0.3,-0.1),"地理":(0.3,0.1,-0.1),"生物":(0.3,0.1,-0.1),"历史":(0.3,0.1,-0.1),"政治":(0.3,0.1,-0.1),"体育":(0.3,0.1,-0.1),"音乐":(0.3,0.1,-0.1),"画画":(0.3,0.1,-0.1),"物理":(0.3,0.1,-0.1),"化学":(0.3,0.1,-0.1)}

            #print(self.score_record['初一']['期中考试']['语文'])
            current_bonus = subject_bonus[subject]
            
            for i in range (len(score_detail)):
                if score_detail[i]> 90 :
                    self.workload[subject] += current_bonus[0]
                
                elif (score_detail[i] <=90 | score_detail[i] > 80):
                    self.workload[subject] += current_bonus[1]
                
                elif (score_detail[i] < 60 ):
                    self.workload[subject] += current_bonus[2]


        def Package(self,length):
          
            package = {}
           
            for i in range (length):
                self.Exam_offset(False,up_number,down_number)
            
                self.Exam_offset(True,up_number,down_number)
                if time != "中考":
                    Bonus(self,self.score_detail,self.subject_list[i])                
                package[self.subject_list[i]] = self.score_detail
                self.score_detail = []
           
            return package
        #处理时间参数，使得输入的时间字符串与相关数据建立关系，精简代码

        period = {"初一":self.seventh,"初二":self.eighth,"初三":self.nineth,"中考":self.end_key}
        length = {"初一": len(self.subject_list)-2,"初二": len(self.subject_list)-1,"初三" : len(self.subject_list),"中考" : len(self.subject_list)}
        data = {"初一":self.seven,"初二":self.eight,"初三":self.nine,"中考":self.end}
         
        for i  in range (len(period[time])):
            pack = Package(self,length[time])
            data[time][period[time][i]] = pack 
        
        self.score_record[time] = data[time]

    



    def Excel(self,time,sort):
        
        if sort == "student":

            ls1 = []
            ls2 = []
            for tup in self.Student:

                ls1.append(tup[0])
                ls2.append(tup[1])


            writer = pd.ExcelWriter('{0}班{1}成绩汇总.xlsx'.format(self.class_id,time), engine='xlsxwriter')

            period = {"初一":self.seventh,"初二":self.eighth,"初三":self.nineth,"中考":self.end_key}


            # Create a Pandas dataframe from some data.
            for i in range (len(period[time])):
                stage = period[time]
                Info = pd.DataFrame({"学号":ls1,"姓名":ls2})
                Data = pd.DataFrame(self.score_record[time][stage[i]])

            # Convert the dataframe to an XlsxWriter Excel object.
                Info.to_excel(writer,sheet_name='{0}班{1}成绩'.format(self.class_id,stage[i]),startcol=0, index=False)
                Data.to_excel(writer,sheet_name='{0}班{1}成绩'.format(self.class_id,stage[i]),startcol=2, index=False)

            # Close the Pandas Excel writer and output the Excel file.
            writer.save()
        
        if sort == "teacher":
            self.bonus_ = []
            for i in range(len(self.subject_list)):
                self.bonus_.append(int(self.workload[self.subject_list[i]]))


            writer = pd.ExcelWriter('{0}班教师绩效汇总.xlsx'.format(self.class_id), engine='xlsxwriter')
            Data = pd.DataFrame({"工号":self.teacher_id,"性别":self.teacher_list,"科目":self.subject_list,"绩效":self.bonus_})
     
            Data.to_excel(writer,sheet_name="绩效",startcol=0,index=False)
            #workload.to_excel(writer,sheet_name="绩效",startcol=len(Data)+1,index=False)

            writer.save()
    
    def Graph(self):
        def Order(self,data):
            result = []

            for i in range(len(data)-1):
                temp = max(data[i:len(data)+1])
                result.append(temp)
            return result
 

        labels = ['frist', 'second', 'third', 'fourth', 'fifth']
        self.bonus_ = Order(self,self.bonus_)
        Stata = self.bonus_[0:5]
        x = np.arange(len(labels))  # the label locations
        width = 0.35  # the width of the bars
        fig, ax = plt.subplots()
        rects1 = ax.bar(x - width/2, Stata, width, label='workload')
        ax.set_ylabel('Workload')
        ax.set_title('Workload of teacher') 
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        ax.legend()
        fig.tight_layout()
        plt.show()

            

