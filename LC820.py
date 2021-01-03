def check(m,n):
    if m == n: return 0
    ml,nl = len(w_set[m]),len(w_set[n])

    if ml>=nl:
        mc = 0
        while w_set[m][ml-1-mc] == w_set[n][nl-1-mc] and mc < nl:
            mc +=1
        if mc == nl: return mc
    else:
        mc = 0
        while w_set[m][ml-1-mc] == w_set[n][nl-1-mc] and mc < ml:
            mc +=1
        if mc == ml: return -mc
    return 0



words= ["time", "me", "me","e","ime"]
w_set = set(words)
l = len(w_set)

al= [len(w) for w in w_set]

sq = [[0 for i in range(l)] for j in range(l)]
for i in range(l):
    for j in range(i,l):
        sq[i][j] = check(i,j)
print(sq)
