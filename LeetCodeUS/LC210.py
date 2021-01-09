numCourses = 3
prerequisites = [[1,0],[1,2],[0,1]]

dic_pre = {}  # pre:[couse]
dic_cos = {}  # cores:[pre]
for i in range(numCourses):
    dic_cos[i] = []
    dic_pre[i] = []
for cos, pre in prerequisites:
        dic_pre[pre].append(cos)
        dic_cos[cos].append(pre)

print(dic_pre)
print(dic_cos)

res = []
next = []
for key in dic_cos:
    if len(dic_cos[key]) == 0:
        next.append(key)
token =[0 for _ in range(numCourses)]
while next:
    print(next)
    tp = []
    for corse in next:
        token[corse] = -1
        res.append(corse)
        if dic_pre[corse]:
            for tak in dic_pre[corse]:
                dic_cos[tak].pop(dic_cos[tak].index(corse))
    for key in dic_cos:
        if len(dic_cos[key]) == 0 and token[key] == 0:
            tp.append(key)
    next = tp[:]

# next = res[:]

print(res)