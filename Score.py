import random
from Student import Student
import pandas as pd
import xlsxwriter
# coding=utf-8

class Class():

    def __init__(self,class_id,class_num):
      
        self.class_id = class_id
        self.class_num = class_num
        self.Student = []
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
        for i in range(len(after)):
            change = abs(after[i] - before[i])
            summary += change
        if summary <=300:
            return True
        else:
            return False
        
 
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


        def Package(self,length):
          
            package = {}
           
            for i in range (length):
                self.Exam_offset(False,up_number,down_number)
            
                self.Exam_offset(True,up_number,down_number)

                package[self.subject_list[i]] = self.score_detail
                self.score_detail = []
           
            return package
        #处理时间参数，使得输入的时间字符串与相关数据建立关系，精简代码

        period = {"初一":self.seventh,"初二":self.eighth,"初三":self.nineth,"中考":self.end_key}
        length = {"初一":len(self.subject_list)-2,"初二":self.subject_list)-1,"初三":len(self.subject_list),"中考":len(self.subject_list)}
        data = {"初一":self.seven,"初二":self.eight,"初三":self.nine,"中考":self.end}
        
        for i  in range (len(period[time])):
            pack = Package(self,length[time])
            data[time][period[time][i]] = pack 
        
        self.score_record[time] = data[time]

    
    def Bonus(self,bonus):
        subject_bonus = bonus





    def Excel(self,time):

        ls1 = []
        ls2 = []
        for tup in self.Student:

            ls1.append(tup[0])
            ls2.append(tup[1])


        writer = pd.ExcelWriter('{0}班级{1}成绩汇总.xlsx'.format(self.class_id,time), engine='xlsxwriter')

        period = {"初一":self.seventh,"初二":self.eighth,"初三":self.nineth,"中考":self.end_key}


        # Create a Pandas dataframe from some data.
        for i in range (len(period[time])):
            Info = pd.DataFrame({"学号":ls1,"姓名":ls2})
            Data = pd.DataFrame(self.score_record[time][period[time]])

        # Convert the dataframe to an XlsxWriter Excel object.
            Info.to_excel(writer,sheet_name='{0}班{1}成绩'.format(self.class_id,period[time]),startcol=0, index=False)
            Data.to_excel(writer,sheet_name='{0}班{1}成绩'.format(self.class_id,period[time]),startcol=2, index=False)

 

        # Close the Pandas Excel writer and output the Excel file.
        writer.save()

        

    




