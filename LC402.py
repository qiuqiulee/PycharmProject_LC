num ="10200"
k = 1

n = len(num)
tp = []
for i in range(k):
    tp.append(int(num[i]))
res = []
for i in range(k,n):
    tp.append(int(num[i]))
    target = min(tp)
    while tp[0] != target:
        tp.pop(0)
    res.append(str(tp[0]))
    tp.pop(0)
s = ''
while res[0] =='0':
    res.pop(0)
print(s.join(res))