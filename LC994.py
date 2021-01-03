grid = [[2,1,1],[1,1,0],[0,1,1]]
m = len(grid)
n = len(grid[0])
fresh = 0
que = []
for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            fresh += 1
        elif grid[i][j] == 2:
            que.append([i, j])
day = 0
dirc = [[-1, 0], [1, 0], [0, -1], [0, 1]]
while que and fresh>0:
    l = len(que)
    day += 1
    for i in range(l):
        x,y = que.pop(-)

        for dx, dy in dirc:
            if 0 <= x + dx < m and 0 <= y + dy < n and grid[x + dx][y + dy] == 1:
                grid[x + dx][y + dy] = 2
                fresh -= 1
                que.append([x + dx, y + dy])
    print(grid,day)