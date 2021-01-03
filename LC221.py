matrix = [["0","0","0","1"],["1","1","0","1"],["1","1","1","1"],["0","1","1","1"],["0","1","1","1"]]
def checksq(x,y):
    bc = dp[x-1][y-1]
    tx = x
    ty = y
    csb = 0
    while bc>0:
        if dp[tx-1][y] >=1 and dp[x][ty-1] >= 1:
            tx-=1
            ty-=1
            bc-=1
            csb +=1
        else:
            return csb
    return csb


m = len(matrix)
n = len(matrix[0])

dp= [[int(matrix[i][j]) for j in range(n)] for i in range(m)]
res = 0
for i in range(m):
    for j in range(n):
        dp[i][j] = int(matrix[i][j])
        if (i!=0) and (j!=0):
            if dp[i][j] == 1 and dp[i-1][j-1]>0 :
                dp[i][j] = 1 +checksq(i,j)
        res = max(res, dp[i][j])
print(res)

