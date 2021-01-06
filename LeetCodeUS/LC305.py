def numIslands2(m, n, positions):
    grid = [['0' for j in range(n)] for i in range(m)]
    dirc = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    res = 0
    ans = []
    for ox, oy in positions:
        grid[ox][oy] = "1"
        flg = True
        for dx, dy in dirc:
            if 0 <= ox + dx < m and 0 <= oy + dy < n and grid[ox + dx][oy + dy] == "1":
                flg = False
        if flg:
            res += 1
        ans.append(res)
    return ans


print(numIslands2(2,2,[[0,0],[1,1],[0,1]]))