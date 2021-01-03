def getmid(a,w):
    l = len(a)
    i = 0
    j = l - 1
    while i < j:

        m = (i + j) // 2
        if a[m] == w:
            return m
        if a[m] > w:
            j = m
        else:
            i = m + 1
    return i - 1

# print(getmid([1,2,3,4,5,6,7],3.5))


ring = "nyngl"
key = "yyynnnnnnlllggg"
newring = ring *3
n = len(ring)
dic ={}
for i in range(3*n):
    if newring[i] not in dic:
        dic[newring[i]] = [i]
    else:
        dic[newring[i]].append(i)
m = len(key)
p = n
res = 0
for w in range(m):
    if w == 0:
        npt = getmid(dic[key[w]], p)
        if p - dic[key[w]][npt] < dic[key[w]][npt + 1] - p:  # close left
            res += p - dic[key[w]][npt]
            p = dic[key[w]][npt] % n + n
        else:
            res += dic[key[w]][npt + 1] - p
            p = dic[key[w]][npt + 1] % n + n
    if w > 0 and key[w] != key[w-1]:
        npt = getmid(dic[key[w]], p)
        if p - dic[key[w]][npt] < dic[key[w]][npt+1] - p: # close left
            res += p - dic[key[w]][npt]
            p = dic[key[w]][npt] % n + n
        else:
            res += dic[key[w]][npt+1] - p
            p = dic[key[w]][npt+1] % n + n
    print(key[w],res)
print(res+m)

ring = "nyngl"
key = "yyynnnnnnlllggg"