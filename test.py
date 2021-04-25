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
    n = (46, 54, 90, 57, 68, 65, 62, 82, 61, 63, 78, 83, 60, 58, 75, 51, 79, 51, 46, 78, 86, 88, 60, 84, 76, 91, 82, 52, 72, 45, 68, 73, 78, 77, 93, 60, 53, 53, 55, 49, 47, 
85, 83, 92, 51, 71, 87, 49, 95, 90, 64, 92, 60, 80, 52, 95, 56, 74, 66, 80)
   #print(order(n))  
    #ScoreStata(n)
    subject = {"语文":(1,0.3,-0.1),"数学":(1,0.3,-0.1),"英语":(1,0.3,-0.1),"地理":(0.3,0.1,-0.1),"历史":(0.3,0.1,-0.1),"政治":(0.3,0.1,-0.1),"体育":(0.3,0.1,-0.1),"音乐":(0.3,0.1,-0.1),"画画":(0.3,0.1,-0.1),"物理":(0.3,0.1,-0.1),"化学":(0.3,0.1,-0.1)}
    print(len(subject))
    print(subject["语文"])