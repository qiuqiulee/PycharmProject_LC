points = [[1,3],[-2,2]]
K= 1
dic ={}
for i ,n in enumerate(points):
    if n[0 ]**2 + n[1 ]**2 in dic:
        dic[n[0 ]**2 + n[1 ]**2].append(i)
    else:
        dic[n[0 ]**2 + n[1 ]**2] = [i]
cand = list(dic.keys())
cand.sort()
res= []
for i in cand:
    for ele in dic[i]:
        res.append(ele)
        K-=1
        if K == 0:
            print(res)