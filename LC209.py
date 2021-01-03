nums = [2,3,1,2,4,3]
s = 7



l = len(nums)

left = 0
cur = 0
res =10000
for right in range(l):
    cur +=nums[right]
    while cur >=s:
        res = min(res, right-left+1)
        cur -= nums[left]
        left += 1
print([0]+nums)