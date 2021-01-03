def qpl(nums,i):
    if i == n:
        a = nums.copy()
        res.append(a)
    for j in range(i,n):
        nums[i],nums[j] = nums[j],nums[i]
        qpl(nums,i+1)
        nums[j],nums[i] = nums[i],nums[j]

nums = [1,2,3]
n = len(nums)
res =[]
qpl(nums,0)
print(res)