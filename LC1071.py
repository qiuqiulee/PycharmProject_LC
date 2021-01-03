str1 = 'abcabcabcabc'
str2 ="abc"
l1 = len(str1)
u1 =[]

for i in range(1,l1+1):
    if l1 % i ==0:
        unit_len = int(l1/i)
        if str1[0:unit_len] * i ==str1:
            u1.append(str1[0:unit_len])

l2 = len(str2)

u2 =[]
for i in range(1,l2+1):
    if l2% i ==0:
        unit_len = int(l2/i)
        if str2[0:unit_len] * i ==str2:
            u2.append(str2[0:unit_len])

uu= [x for x in u1 if x in u2]
print(uu)