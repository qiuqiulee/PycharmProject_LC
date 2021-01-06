def dfs(a):
    for j in range(n):
        if a!=j and isConnected[a][j] == 1 and flg[j]==0:
            flg[j] = flg[a]
            dfs(j)

isConnected =[[1,0,0],[0,1,0],[0,0,1]]
n = len(isConnected)
flg = [0 for i in range(n)]

for i in range(n):
    if flg[i] == 0:
        flg[i] = max(flg)+1
        dfs(i)

print(flg)
print(max(flg))