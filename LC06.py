import math

s = "PAYPALISHIRING"
numRows = 3
oneset = 2 * numRows - 2
n = len(s)
numCo = math.ceil(n / oneset) * (numRows - 1)
outarr = [['xx' for _ in range(numCo)] for _ in range(numRows)]
i = 0
dn = 0
x = 0
y = 0
ur = 0
while i < n:
    while dn < numRows and i < n:
        outarr[x][y] = s[i]
        dn += 1
        x += 1
        i += 1
    x-=1
    while ur < numRows - 2 and i < n:
        x -= 1
        y += 1
        ur += 1
        outarr[x][y] = s[i]
        i += 1
    x -= 1
    y += 1

    dn = 0
    ur = 0
res =''
for i in range(numRows):
    for j in range(numCo):
        if outarr[i][j] !='xx':
            res+=outarr[i][j]
print(res)