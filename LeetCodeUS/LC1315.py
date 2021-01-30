def minDifficulty(jobDifficulty, d) -> int:
    N = len(jobDifficulty)
    dp = [[None for _ in range(N)] for _ in range(d)]

    for i in range(0 + N - (d - 1)):
        dp[0][i] = max(jobDifficulty[0:i + 1])

    for day in range(1, d):
        for job in range(day, day + N - (d - 1)):
            dp[day][job] = 99999
            for i in range(day, job+1):
                val = max(jobDifficulty[i:job + 1]) + dp[day-1][i - 1]
                dp[day][job] = min(val, dp[day][job])
    if dp[d - 1][N - 1] == None:
        return -1
    return dp[d - 1][N - 1]

jobDifficulty = [11,111,22,222,33,333,44,444]
d = 5
print(minDifficulty(jobDifficulty,d))