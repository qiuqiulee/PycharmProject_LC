s = 'aabcbbbc'
p = 'a*c'
s_len = len(s)
p_len = len(p)

# dp[i][j] 表示 s[:i] 与 p[:j] 是否匹配，各自前 i、j 个是否匹配
dp = [[False] * (p_len + 1) for _ in range(s_len + 1)]
dp[0][0] = True

# s 为空串
for j in range(1, p_len + 1):
    # 若 p 的第 j 个字符 p[j - 1] 是 '*'
    # 说明第 j - 1、j 位可有可无
    # 那么如果前 j - 2 个已经匹配上，前 j 个也可以匹配上
    if p[j - 1] == '*':
        dp[0][j] = dp[0][j - 2]

for i in range(1, s_len + 1):
    for j in range(1, p_len + 1):
        if p[j - 1] in {s[i - 1], '.'}:
            dp[i][j] = dp[i - 1][j - 1]
        elif p[j - 1] == '*':
            if p[j - 2] in {s[i - 1], '.'}:
                dp[i][j] = dp[i][j - 2] or dp[i - 1][j - 2] or dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 2]
print(dp[s_len][p_len])