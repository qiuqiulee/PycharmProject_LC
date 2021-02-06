def subarraySum(nums, k):
    res = 0
    dic = {}
    dic[0] = 1
    m = len(nums)
    temp_sum = 0
    for i in range(m):
        temp_sum += nums[i]
        if temp_sum in dic:
            dic[temp_sum] += 1
        else:
            dic[temp_sum] = 1
    key_list = list(dic.keys())
    for key in key_list:
        if key + k in dic:
            res += dic[key] * dic[key + k]
    return res
n = [1,2,3]
k = 2
print(subarraySum(n,k))