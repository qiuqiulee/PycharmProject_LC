tree = [3]

n = len(tree)
i = 0
j = 0
ft = set()
res = 0
while j < n:
    ft = set(tree[i:j])
    if len(ft) >2:
        i += 1
    elif len(ft) == 2 and tree[j] not in ft:
        j+=1
    else:
        j += 1
        res = max(res, j - i)


print(res)