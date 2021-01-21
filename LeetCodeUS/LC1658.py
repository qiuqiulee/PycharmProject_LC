# def minOperations(self, nums: List[int], x: int) -> int:
nums =[1,1]
x = 3
m = len(nums)
arr = [0 for _ in range(2*m+1)]

for i in range(m+1, 2 * m+1):
    arr[i] = arr[i - 1] + nums[i - m-1]
for i in range(m - 1, -1, -1):
    arr[i] = arr[i+1]+nums[i]
dic ={}
for i,num in enumerate(arr):
    if i>=m:
        if num in dic:
            dic[num].append(i)
        else:
            dic[num] = [i]
res =9999999
for i in range(m+1):
    rest = x - arr[i]
    if rest in dic:
        res = min(res,dic[rest][0]-i)

print(dic)
print(res)