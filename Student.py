# coding=utf-8
import random
class Student():
    std_count = 0    
    def __init__(self,year,fname_firstname,fname_lastname):
        
        self.year = year
        self.firstname = fname_firstname
        self.lastname = fname_lastname
        Student.std_count += 1
        self.sid = str(self.year)+ str(self.std_count).zfill(2)
    def GetName(self):
        path1 = "assets/" + "firstname.txt"
        path2 = "assets/" + "lastname.txt"
        try:#文件第一个空行占三位，之后每个字占1位，换行占2位
            fo = open(path1,"r",encoding="utf-8")
            content = fo.read()
            content_single = content[0:550]            
            spilt = content_single.split()
            name_list = []
            for group in spilt:
                for i in range(len(group)):
                    name_list.append(group[i])
            #print(name_list)

        except Exception:
            print("Failed to load files needed")

        try:
            fo = open(path2,"r",encoding="utf-8")
            name_list_last = fo.read().split(",")
            #print(name_list_last)
            fo.close()
        except Exception:
            print("Failed to load files needed")

        first_name_index = random.randint(0, len(name_list)-1)
        last_name_index = random.randint(0, len(name_list_last)-1)
        stdname = name_list[first_name_index] + name_list_last[last_name_index]
        fo.close()
        return stdname
        


    def display(self,type):
        if(self.type == "name"):
            print("Name" + self.name)
        if(self.type == "sid"):
            print("学号：" + sid)
    