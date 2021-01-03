graph = [[1],[0,3],[3],[1,2]]
res = True
m = len(graph)
cl = [0 for _ in range(m)]
for i in range(m):
    if cl[i] == 0:
       cl[i] = 1
    n = len(graph[i])
    for j in range(n):
        if cl[graph[i][j]] == 0:
            cl[graph[i][j]] = cl[i]*(-1)
        elif cl[graph[i][j]]*cl[i] ==1:
            res = False
