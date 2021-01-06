def numIslands2(m, n, positions):
    def numIslands(grid):
        def dfs(x, y):
            grid[x][y] = "0"
            for dx, dy in dirc:
                if 0 <= x + dx < m and 0 <= y + dy < n:
                    if grid[x + dx][y + dy] == "1":
                        dfs(x + dx, y + dy)
        dirc = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        res = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    res += 1
                    dfs(i, j)
        return res


    grid = [["0" for j in range(n)] for i in range(m)]
    ans = []
    for ox, oy in positions:
        grid[ox][oy] = '1';
        grid_temp = [x[:] for x in grid]
        ans.append(numIslands(grid_temp))
    return ans

print(numIslands2(3,3,[[0,0],[0,1],[1,2],[2,1]]))