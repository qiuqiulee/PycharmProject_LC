import random


def solution2(nums):
    n = len(nums)

    def step1():
        for i in range(n):
            if nums[i] > 0:
                return i
        return -1

    def step2(idx, x):
        for i in range(idx, n):
            if nums[i] >= x:
                nums[i] -= x
            else:
                break

    res = 0
    # print(nums)
    while True:
        idx = step1()
        if idx == -1:
            return res
        x = nums[idx]
        step2(idx, x)

        res += x
        # print(nums,res)
nums = [random.randint(1,10) for _ in range(5)]
# nums = [3, 2, 1, 10, 6, 6, 9, 8, 4, 9]
nums = [1,3,4,3,4,5,6,4]
print(solution2(nums))


def sumOfFirst(nums):
    m = len(nums)
    i = 0
    res = 0
    while True:
        while i < m and nums[i] <= 0:
            i += 1
        if i == m:
            return res
        x = nums[i]
        while i < m and nums[i] >= x:
            nums[i] -= x
            i += 1
        res += x
        print(nums,x)
        i = 0

nums = [1]
print(sumOfFirst(nums))
