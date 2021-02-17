def climbingStaircase(n, k):
    def bt(path, dis):
        if dis == n:
            tppath = path[:]
            res.append(tppath)
        else:
            for i in range(1, k + 1):
                if dis + i > n:
                    break
                path += [i]
                bt(path, dis + i)
                path.pop(-1)

    res = []
    bt([], 0)
    return res
print(climbingStaircase(4,2))