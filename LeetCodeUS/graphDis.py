def graphDistances(g, s):
    def dfs(visited, dis):
        nonlocal dic
        if visited[-1] == s and visited[0] in dic and dic[visited[0]][0] > dis:
            dic[visited[0]][0] = dis
            dic[visited[0]][1] = visited
        if visited[-1] == s and visited[0] not in dic:
            dic[visited[0]] = [4000,[]]
            dic[visited[0]][0] = dis
            dic[visited[0]][1] = visited
        if visited[-1]!=s:
            for j in range(m):
                if j not in visited  and g[visited[-1]][j] >= 0:
                    if j in dic and j !=s:
                            dfs(visited+dic[j][1],dis+g[visited[-1]][j]+dic[j][0])
                    elif (j not in dic or j ==s) :
                        dfs(visited + [j], dis + g[visited[-1]][j])

    m = len(g)

    for i in range(m-1):
        for j in range(i+1,m):
            g[i][j],g[j][i] = g[j][i],g[i][j]
    print(g)
    dic = {}
    dic[s] = [0,[s]]
    for i in range(m):
        if i not in dic:
            dfs([i],0)
            newpath = dic[i][1][:]
            newdis = dic[i][0]
            while len(newpath) >2:
                stpt = newpath.pop(0)
                newdis -=g[stpt][newpath[0]]
                if stpt not in dic:
                    ddis = newdis
                    dpath = newpath[:]
                    dic[stpt] = [ddis,dpath]
    res = [0] * m
    for i in range(m):
        res[i] = dic[i][0]
    print(dic)
    return res

g = [[-1,3,2,-1],
 [3,-1,-1,1],
 [2,-1,-1,3],
 [-1,1,3,-1]]
s= 3

print(graphDistances(g,s))