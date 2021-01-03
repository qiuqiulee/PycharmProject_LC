grid = [
  ["0","0","0","0","0"],
  ["0","0","0","0","0"],
  ["0","0","0","0","0"],
  ["0","0","0","0","0"]
]



def checkit(x, y):
    ck[x][y] = 1
    for tx, ty in dirc:
        if 0 <= x + tx < m and 0 <= y + ty < n and grid[x + tx][y + ty] == '1' and ck[x + tx][y + ty] == 0:
            checkit(x + tx, y + ty)


m = len(grid)
n = len(grid[0])
dirc = [[0, -1], [0, 1], [1, 0], [-1, 0]]
res = 0
ck = [[0 for _ in range(n)] for _ in range(m)]
for i in range(m):
    for j in range(n):
        if ck[i][j] == 0 and grid[i][j] == '1':
            res += 1
            checkit(i, j)
print(res)
