nums = [1,2,3]
res = []
n = len(nums)


def helper(i, tmp):
    res.append(tmp)
    for j in range(i, n):
        helper(j + 1, tmp + [nums[j]])


helper(0, [])

print(res)