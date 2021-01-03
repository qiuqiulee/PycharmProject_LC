n = 12
mxlst = int(n ** 0.5)
arr = [0] * mxlst
for i in range(mxlst):
    arr[i] = (i + 1) ** 2
arr =arr[::-1]
print(arr)
