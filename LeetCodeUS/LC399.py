equations = [["a", "b"], ["b", "c"], ["bc", "cd"]]
values = [1.5, 2.5, 5.0]

dic = {}
m = len(equations)
for i in range(m):
    if equations[i][0] not in dic:
        dic[equations[i][0]] = {}
        dic[equations[i][0]][equations[i][0]] = 1
    if equations[i][1] not in dic:
        dic[equations[i][1]] = {}
        dic[equations[i][1]][equations[i][1]] = 1
    dic[equations[i][0]][equations[i][1]] = values[i]
    dic[equations[i][1]][equations[i][0]] = 1 / values[i]

print(dic)

for key in dic:
    seen = [key]
    nextvisit = []
    for ele in dic[key].keys():
        if ele not in seen:
            nextvisit.append(ele)
    temp = []
    while nextvisit:
        for ele in nextvisit:
            ratio = dic[key][ele]
            seen.append(ele)
            for ele2 in dic[ele]:
                if ele2 not in seen:
                    dic[key][ele2] = ratio * dic[ele][ele2]
                    temp.append(ele2)
        nextvisit = temp
print(dic)


