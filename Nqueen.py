def check(tq, r, c):
    if r == 0:
        return True
    for j in range(r):
        if tp[j] == c or j + tp[j] == c + r or j - tp[j] == r - c:
            return False
    return True


def bk(tp):
    if not -1 in tp:
        a = tp[:]
        for w in range(n):
            a[w] += 1
        res.append(a)
    else:
        r = tp.index(-1)
        for c in range(n):
            if check(tp, r, c):
                tp[r] = c
                bk(tp)
                tp[r] = -1


n = 4
res =[]
tp = [-1]*n
bk(tp)

print(res)
ans =[]
for x in res:
    t_as = []
    for ele in x:
        st = "." * ele +"Q" +"."*(n-1-ele)
        t_as.append(st)
    ans.append([t_as])
print(ans)