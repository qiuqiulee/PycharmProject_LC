s = 'abcabcbb'
m = len(s)
dp = [[1 for _ in range(m)] for _ in range(m)]
res = 1
for i in range(m-1):
    for j in range(i+1, m):
        print(i, j)
        if s[j] not in s[i:j]:
            dp[i][j] = dp[i][j - 1] + 1
            res = max(res,dp[i][j])
        else:
            break

print(dp)
print(res)