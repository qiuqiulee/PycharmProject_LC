# dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
dungeon = [[-2, -3, 3]]
m = len(dungeon)
n = len(dungeon[0])
dp = [[0 for _ in range(n)] for _ in range(m)]

for i in range(m - 1, -1, -1):
    for j in range(n - 1, -1, -1):
        if i == m - 1 and j == n - 1:
            dp[i][j] = dungeon[i][j]
            if dp[i][j] > 0:
                dp[i][j] = 0
        if i == m - 1 and j != n - 1:
            dp[i][j] = dungeon[i][j] + dp[i][j + 1]
            if dp[i][j] > 0:
                dp[i][j] = 0
        if i != m - 1 and j == n - 1:
            dp[i][j] = dungeon[i][j] + dp[i + 1][j]
            if dp[i][j] > 0:
                dp[i][j] = 0
        if i != m - 1 and j != n - 1:
            dp[i][j] = dungeon[i][j] + max(dp[i][j + 1], dp[i + 1][j])
            if dp[i][j] > 0:
                dp[i][j] = 0
print(dp)
