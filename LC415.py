num1 = '0'
num2 ='0'
m = len(num1)
n = len(num2)
if m < n:
    num1, num2 = num2, num1
    m, n = n, m
num1 = "0" + num1

m += 1
num2 = "0"*(m-n) +num2
i = m - 1

ad = 0
res = ''
while i >= 0:
    yu = (int(num1[i]) + int(num2[i]) + ad) % 10
    ad = (int(num1[i]) + int(num2[i]) + ad) // 10
    res = str(yu) + res
    i -= 1

i = 0
while i<m and res[i] =='0':
    i+=1
print(res[i:])