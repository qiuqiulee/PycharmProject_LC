def sqdt(x, y):
    px = x
    py = y
    tgt = area[x - 1][y - 1]
    stp = 1
    while tgt > 0:
        px -= 1
        py -= 1

        if matrix[px][y] == '1' and matrix[x][py] == '1':
            tgt -= 1
            stp += 1
        else:
            return stp
    return area[x - 1][y - 1] + 1

matrix = [["0","0","0","1"],
          ["1","1","0","1"],
          ["1","1","1","1"],
          ["0","1","1","1"],
          ["0","1","1","1"]]
            # [[0, 0, 0, 1],
            #  [1, 1, 0, 1],
            #  [1, 2, 1, 1],
            #  [0, 1, 1, 2],
            #  [0, 1, 2, 2]]
m = len(matrix)
n = len(matrix[0])
area = [[0 for _ in range(n)] for _ in range(m)]
for i in range(m):
    if matrix[i][0] == '1':
        area[i][0] = 1
for j in range(n):
    if matrix[0][j] == '1':
        area[0][j] = 1
res = 0
for i in range(1, m):
    for j in range(1, n):
        if matrix[i][j] == '1':
            area[i][j] = sqdt(i, j)
            res= max([res,area[i][j] ])
print(res)