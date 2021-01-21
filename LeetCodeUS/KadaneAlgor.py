a = [-2, -3, 4, -1, -2, 1, 5, -3]
m = len(a)
dp = [0 for _ in range(m)]

for i in range(1,m):
    dp[i] = max(dp[i-1]+a[i],0)
print(dp)