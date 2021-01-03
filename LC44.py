s = "adceaab"
p = "*a*b"

p_c =[]
l_p = len(p)
for i in range(l_p):
    if p[i].isalpha():
        p_c.append(i)


match = []

for i in range(len(p_c)):
    match.append([j for j in range(len(s)) if s[j] == p[p_c[i]]])


tst = []
for i in  range(len(match)):
    stpt = -1
    crr=[]
    x = match[i]
    for ele in x:
       if ele > stpt:
           crr.append(ele)
           stpt = ele
           continue


    tst.append(crr)
print(tst)