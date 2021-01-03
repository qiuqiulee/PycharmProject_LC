R =1
C = 2
r0 = 0
c0 =0

res = []
dic = {}
for i in range(R):
    for j in range(C):
        dis = abs(i-r0)+abs(j-c0)
        if dis in dic:
            dic[dis].append([i,j])
        else:
            dic[dis] = [[i,j]]
key = list(dic.keys())
key.sort()
for k in key:
    for i in range(len(dic[k])):
        res.append([dic[k][i][0],dic[k][i][1]])
print(res)