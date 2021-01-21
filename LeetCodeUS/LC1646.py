a = [0 for _ in range(100)]
a[1] = 1
for i in range(100):
    if i%2 ==0:
        a[i] = a[i//2]
    else:
        a[i] = a[i//2] + a[i//2+1]
print(a)