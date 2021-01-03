intervals =[[1,3],[2,6],[8,10],[15,18]]
intervals.sort(key=lambda x:x[0])
m = len(intervals)
res = []
res.append(intervals[0])

for i in range(1,m):
    if intervals[i][0] > res[-1][-1]:
        res.append(intervals[i])
    elif intervals[i][1] > res[-1][1]:
        res[-1][1] = intervals[i][1]
print(res)