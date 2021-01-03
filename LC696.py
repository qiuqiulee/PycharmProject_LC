s ='0011'
m = len(s)
i = 0
ls = []
while i < m:
    flag = s[i]
    j=i
    ct = 0
    while j<m and s[i] == s[j]  :
        ct+=1
        j+=1
    ls.append(ct)
    i = j
n = len(ls)
print(ls)