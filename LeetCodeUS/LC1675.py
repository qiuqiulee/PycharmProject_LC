import heapq
def minimumDeviation1(A):
    pq = []
    for a in A:
        heapq.heappush(pq, -a * 2 if a % 2 else -a)
    res = float('inf')
    mi = -max(pq)
    while len(pq) == len(A):
        a = -heapq.heappop(pq)
        res = min(res, a - mi)
        if a % 2 == 0:
            mi = min(mi, a / 2)
            heapq.heappush(pq, -a / 2)
    return res

def minimumDeviation2(A):
        pq = []
        for a in A:
            heapq.heappush(pq, [a / (a & -a), a])
        res = float('inf')
        ma = max(a for a, a0 in pq)
        while len(pq) == len(A):
            a, a0 = heapq.heappop(pq)
            res = min(res, ma - a)
            if a % 2 == 1 or a < a0:
                ma = max(ma, a * 2)
                heapq.heappush(pq, [a * 2, a0])
        return res
print(minimumDeviation1([4,1,5,20,3]))
print(minimumDeviation2([4,1,5,20,3]))