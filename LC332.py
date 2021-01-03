# import numpy as np
tic =  [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# tc = np.array(tic)
# ori = np.array(tc[:,0])
# des = np.array(tc[:,1])
# res = []
# fd = "JFK"
# while ori.size >0:
#     res.append(fd)
#     ls = list(np.where(ori==fd))
#     if len(ls[0]) > 1:
#         ls_d = des[ls]
#         fd= min(ls_d)
#         ds_lis = np.where(des == fd)
#         fd_index =np.intersect1d(ds_lis, ls)[0]
#     else:
#         fd= des[ls[0][0]]
#         fd_index = ls[0][0]
#     ori = np.delete(ori,fd_index)
#     des = np.delete(des,fd_index)

# res.append(fd)
# print(res)
import collections

d = collections.defaultdict(list)   #邻接表
for f, t in tic:
    d[f] += [t]         #路径存进邻接表
for f in d:
    d[f].sort()         #邻接表排序
ans = []
def dfs(f):             #深搜函数
    while d[f]:
        dfs(d[f].pop(0))#路径检索
    ans.insert(0, f)    #放在最前
dfs('JFK')
print(ans)