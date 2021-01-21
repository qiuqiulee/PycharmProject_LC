intervals =[[2,3],[0,1],[1,2],[3,4],[4,5],[1,1],[0,1],[4,6],[5,7],[1,1],[3,5]]
dic = {}
for start, end in intervals:
    if start not in dic:
        dic[start] = [end]
    else:
        dic[start].append(end)
lst = list(dic.keys())
lst.sort()
m = len(lst)
i = 0
res = []

while i<m:
    start = lst[i]
    end = dic[lst[i]][-1]

    while i < m and lst[i] <= end:
        end = max(end,max(dic[lst[i]]))
        i+=1
    res.append([start,end])

print(res)
