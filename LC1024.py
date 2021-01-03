clips =[[7,9],[5,9],[10,10],[5,10],[8,10],[2,6],[7,9],[7,10],[4,5]]
T = 2
es = []
for a, b in clips:
    es.append(b)

maxl = [0] * (max(max(es), T)+1)
for a, b in clips:
    maxl[a] = max(maxl[a], b)

pre = 0
last = 0
res = 0

for i in range(T):
    last = max(last, maxl[i])
    if i == last:
        print(-1)
        exit()
    if i == pre:
        res += 1
        pre = last
print(res)