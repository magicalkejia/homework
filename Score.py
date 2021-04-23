import random
from Student import Student
import pandas as pd
import xlsxwriter


class Class():
    index_record = []
    def __init__(self,class_id,class_num):
        self.subject = subject
        self.class_id = class_id
        self.class_num = class_num
        self.Student = []
 
        self.score_detail = []
        self.score_record = []
        
        self.offset_up = 5
        self.offset_down = 5
    
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
        
    
    def Exam(self,teacher_attr,subject):
       
        if teacher_attr == "serious":
            up_number = 0.05*self.class_num
            down_number = 0.03*self.class_num


        if teacher_attr == "casual":
             up_number = 0.03*number
             down_number = 0.05*number
    

        self.Exam_offset(False,up_number,down_number)
    
        self.Exam_offset(True,up_number,down_number)

        self.score_record.append(self.score_detail)
        self.score_detail = []



    def Excel(self):
        print(self.Student)
        print(self.score_record)
        ls1 = []
        ls2 = []
        for tup in self.Student:

            ls1.append(tup[0])
            ls2.append(tup[1])

        # Create a Pandas dataframe from some data.
        Data = pd.DataFrame({'学号': ls1,'名字': ls2,'语文': self.score_record[0]})
       
   
        writer = pd.ExcelWriter('ClassScore.xlsx', engine='xlsxwriter')

        # Convert the dataframe to an XlsxWriter Excel object.
        Data.to_excel(writer,sheet_name='{0}班级{1}成绩'.format(self.class_id,"期中"),startcol=0, index=False)
 

        # Close the Pandas Excel writer and output the Excel file.
        writer.save()

        

    




