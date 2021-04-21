import random
import pandas as pd
import MainTask from MainTask


class Class():
    def __init__(self,subject,class_id,class_num):
        self.subject = subject
        self.class_id = class_id
        self.class_num = class_num
        self.Student = []

    
        
        self.score_detail = []
        self.score_record = ()
        
        self.offset_up = 5
        self.offset_down = 5
    
    def CreateStudent(self):
        for i in range(self.class_num):
            tup = ()
            current = Student(2021,"firstname.txt","lastname.txt")
            tup.append(current.sid)
            tup.append(current.GetName())
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
                    num = random.randint(45,95)
                    temp.append(num)               
                self.score_detail = temp
                del temp                   

    
            rmdata(self)


     

    def ScoreStata(self,data):
        origin = data
        order = data
        index = []
        for i in range(len(order)-1):
            minindex = i
            for j in range(i+1,len(order)):
                if order[j] < order[minindex]:
                    minindex = j
                if i != minindex:
                    order[i], order[minindex] = order[minindex],order[i]
      
        for i in range(len(origin)-1):
            for j in range(len(order)-1):
                if origin[i] == order[j]:
                    index.append(j)
      
        return index
        del index
        


    def CheckOffset(self,before,after):
        summary = 0
        #ls = []
        for i in range(len(after)-1):
            change = abs(after[i] - before[i])
            summary += change
        if summary <=300:
            return True
        else:
            return False
        
        



    
    
    def Exam(self,teacher_attr):
       
        if teacher_attr == "serious":
            up_number = 0.05*self.class_num
            down_number = 0.03*self.class_num

            #print(Score_list)
        
        if teacher_attr == "casual":
             up_number = 0.03*number
             down_number = 0.05*number

        def attempt(self,up_number,down_number):
            self.Exam_offset(False,up_number,down_number)
            

            index_before = self.ScoreStata(self.score_detail)

            self.Exam_offset(True,up_number,down_number)

            index_after =  self.ScoreStata(self.score_detail)

            result = self.CheckOffset(index_before,index_after)
            if (result == True):
                self.score_record.append(self.score_detail)
                self.score_detail = []
            if (result == False):
                self.score_detail = []
                attempt(self,up_number,down_number)

          
        attempt(self,up_number,down_number)

    def Excel(self):
        print(self.Student)
        print(self.score_record)
        ls1 = []
        ls2 = []
        for tup in self.Student:

            ls1.append(tup[0])
            ls2.append(tup[1])

        # Create a Pandas dataframe from some data.
        std_id = pd.DataFrame({'Sid': ls1})
        std_name = pd.DataFrame({'Name': ls2})
        score = pd.DataFrame({'Data': self.score_record[0]})

        # Create a Pandas Excel writer using XlsxWriter as the engine.
        writer = pd.ExcelWriter('ClassScore.xlsx', engine='xlsxwriter')

        # Convert the dataframe to an XlsxWriter Excel object.
        std_id.to_excel(writer,sheet_name='ClassScore_{0}'.format(self.class_id))
        std_name.to_excel(writer,sheet_name='ClassScore_{0}'.format(self.class_id))
        score.to_excel(writer,sheet_name='ClassScore_{0}'.format(self.class_id))

        # Close the Pandas Excel writer and output the Excel file.
        writer.save()

        

    




