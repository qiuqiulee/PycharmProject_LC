A = ["bella","label","roller"]
n = len(A)
dic = {}
for x in A[0]:
    if x not in dic:
        dic[x] =1
    else:
        dic[x]+=1
for i in range(1,n):
    dict = {}
    for x in A[i]:
        if x not in dict:
            dict[x] = 1
        else:
            dict[x] += 1
    dico = {}
    for y in dict:
        if (y in dict) and (y in dic):
            dico[y] = min(dict[y],dic[y])
    dic = dico

res = []
for x in dic:
    for i in range(dic[x]):
        res.append(x)

print(res)

