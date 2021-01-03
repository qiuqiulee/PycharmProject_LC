points = [[0,1],[1,0]]
K = 1
n = len(points)
dic = {}
for i in range(n):
    dis = points[i][0]**2 + points[i][1]**2
    if dis not in dic:
        dic[dis] = [i]
    else:
        dic[dis].append(i)
res =[]
s_k = sorted(dic.keys())
m = len(s_k)
for i in range(m):
    tl = len(dic[s_k[i]])
    for j in range(tl):
        if K > 0:
            ind = dic[s_k[i]][j]
            res.append([points[ind][0],points[ind][1]])
            K-=1
        else:
            break

print(res)