import numpy as np
matrix = [["0", "1", "1", "0", "1"], ["1", "1", "0", "1", "0"], ["0", "1", "1", "1", "0"], ["1", "1", "1", "1", "0"],
     ["1", "1", "1", "1", "1"], ["0", "0", "0", "0", "0"]]

mt = np.array(matrix)




m = len(mt)
n = len(mt[0])
heng = np.zeros((m,n))
shu = np.zeros((m,n))
area = np.zeros((m,n))
# heng = [[0 for _ in range(n)] for _ in range(m)]
# shu = [[0 for _ in range(n)] for _ in range(m)]

for i in range(m):
    if mt[i][0] == '1':
        heng[i][0] = 1
    for j in range(1, n):
        if mt[i][j] == '1':
            heng[i][j] += heng[i][j - 1]+1
        else:
            heng[i][j] = 0

for j in range(n):
    if mt[0][j] == '1':
        shu[0][j] = 1
    for i in range(1, m):
        if mt[i][j] == '1':
            shu[i][j] += shu[i - 1][j]+1
        else:
            shu[i][j] = 0

for i in range(m):
    for j in range(n):
        if shu[i][j] > 0:
            st = int(i-shu[i][j]+1)
            ed = int(i+1)
            lst= heng[st:ed,j]
            l = len(lst)
            ta = 0
            for k in range(l):
                ta = max(ta,(l-k)*min(lst[k:l]))

            area[i][j]= ta
# print(matrix)
# print(heng)
# print(shu)
print (area)