s2 ='123'
s1 ='abc'

l1,l2= len(s1),len(s2)
res = ''
for i in range(l1):
    res+=s1[i]+s2[i]
res += s2[i+1:]
print(res)
