height = [4,2,0,3,2,5]
m = len(height)
l = [0 for i in range(m)]
r = [0 for i in range(m)]
flg_l = height[0]
flg_r = height[-1]
l[0] = height[0]
r[-1] = height[-1]
for i in range(1, m-1):
    if height[i] > flg_l:
        flg_l = height[i]
    l[i] = flg_l
    if height[m - i - 1] > flg_r:
        flg_r = height[m - i - 1]
    r[m - i - 1] = flg_r

print(l)
print(r)
res = [0 for i in range(m)]
for i in range(m):
    res[i] = max((min(l[i],r[i]) - height[i]),0)
print(res)