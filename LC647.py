s= 'aabbaa'
m = len(s)
hw=[[0 for _ in range(m)] for _ in range(m)]
res = 0
for i in range(m):
    j = i+1
    hw[i][i] = 1
    res += 1
    pi = i
    pj = j
    flg = True
    if pj<m and s[pi] == s[pj]:
        hw[i][j] =1
        res += 1
        j+=1
        while flg and j<m:
            if i-(j-(i+1)) >=0 and s[j] == s[i-(j-(i+1))]:
                hw[i-(j-(i+1))][j] = 1
                j+=1
                res+=1
            else:
                flg = False

    j = i + 1
    while flg and j < m:
        if i-(j-(i)) >=0 and s[j] == s[i-(j-(i))]:
            hw[i - (j - (i))][j] = 1
            res += 1
            j+=1
        else:
            flg = False


print(res)

