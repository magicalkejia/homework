import random
class Teacher():
    teacher_count = 0 
    def __init__(self,fname_firstname,fname_lastname):

        self.firstname = fname_firstname
        self.lastname = fname_lastname
        Teacher.teacher_count += 1
        self.tid = str(self.teacher_count).zfill(6)

    def GetName(self):#读取两个文件的内容，混合生产名字
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
        teacher_name = name_list[first_name_index] + name_list_last[last_name_index]
        fo.close()
        return teacher_name
        