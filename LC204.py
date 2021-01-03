n = 10
res = [2,3]


def ts(x):
    sq = int(x ** 0.5)+1
    t = 3
    while t < sq:
        if x % t == 0:
            return False
        t += 1
    return True


for i in range(5, n , 2):
    if i%3!=0 and ts(i):
        res.append(i)
print(res)
