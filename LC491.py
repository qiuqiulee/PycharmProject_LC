def findSubsequences(nums):
    def helper(start, tmpList):
        if start >= len(nums):
            return

        for i in range(start, len(nums)):
            if nums[i] >= tmpList[-1]:
                tmpList.append(nums[i])
                if len(tmpList) >= 2 and not totalList.count(tmpList):
                    tl = tmpList.copy()
                    totalList.append(tl)
                helper(i + 1, tmpList)
                tmpList.pop()

    totalList = []

    for i in range(len(nums)):
        tmpList = [nums[i]]
        helper(i + 1, tmpList[:])

    return totalList

nums = [2,4,7,8,2,9]

print(findSubsequences(nums))
