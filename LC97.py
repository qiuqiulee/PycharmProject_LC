def isInterleave(s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)
        o = len(s3)
        if m+n!=o:
            return False
        if m + n != o:
            return False
        if not s1:
            if s2 == s3:
                return True
            else:
                return False
        if not s2:
            if s1 == s3:
                return True
            else:
                return False
        if not s1 and not s2:
            if not s3:
                return True
            else:
                return False
        dp = [[False for _ in range(n+1)] for _ in range(m+1)]
        dp[0][0] = True
        for j in range(1, n + 1):
            dp[0][j] = (dp[0][j - 1] and s2[j - 1] == s3[j - 1])
        for i in range(1, m + 1):
            dp[i][0] = (dp[i - 1][0] and s1[i - 1] == s3[i - 1])

        for i in range(1,m+1):
            for j in range(1,n+1):

                    dp[i][j] = ((dp[i-1][j] and s1[i-1] == s3[i+j-1])) or( (dp[i][j-1] and s2[j-1] == s3[i+j-1]))
        return dp[-1][-1]
s1 = "aa"
s2 = "ab"
s3 = "abaa"
print(isInterleave(s1,s2,s3))