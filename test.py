def ScoreStata(data):
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
    print(index)
    #return index
    

if __name__ == "__main__":
    #n = (46, 54, 90, 57, 68, 65, 62, 82, 61, 63, 78, 83, 60, 58, 75, 51, 79, 51, 46, 78, 86, 88, 60, 84, 76, 91, 82, 52, 72, 45, 68, 73, 78, 77, 93, 60, 53, 53, 55, 49, 47, 
    #85, 83, 92, 51, 71, 87, 49, 95, 90, 64, 92, 60, 80, 52, 95, 56, 74, 66, 80)
    #print(order(n))  
    #ScoreStata(n)
    #subject = {"语文":(1,0.3,-0.1),"数学":(1,0.3,-0.1),"英语":(1,0.3,-0.1),"地理":(0.3,0.1,-0.1),"历史":(0.3,0.1,-0.1),"政治":(0.3,0.1,-0.1),"体育":(0.3,0.1,-0.1),"音乐":(0.3,0.1,-0.1),"画画":(0.3,0.1,-0.1),"物理":(0.3,0.1,-0.1),"化学":(0.3,0.1,-0.1)}
    #print(len(subject))
    #print(subject["语文"])
    #nineth = {"第一次月考":0,"第二次月考":0,"期中考试":0,"第三次月考":0,"第四次月考":0,"期末考试":0,"第一次月考（2）":0,"第二次月考（2）":0,"期中考试（2）":0,"第三次月考（2）":0,"第四次月考（2）":0,"期末考试（2）":0,"中考":0}
    # print(len(nineth))
    seventh = ["期中","期末","期中（2）","期末（2）"]
    dict = {}
    dict2 = {}
    for i in range(len(seventh)):
       pack = [(1,2,3),(3,2,1),(1,3,2),(1,2,4)]
       dict[seventh[i]] = pack[i]
       dict2[str(i)] = dict 
    
    length = {"初一":len(seventh)-2,"初二":13-1,"初三":13,"中考":13}
        
    #print(dict2['0']['期中'])
    exit()


