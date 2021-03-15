def recoverArr(nums):
    dic = {}
    for n1,n2 in nums:
        if n1 not in dic:
            dic[n1] = [n2]
        else:
            dic[n1].append(n2)
        if n2 not in dic:
            dic[n2] = [n1]
        else:
            dic[n2].append(n1)

    for key in dic:
        if len(dic[key]) == 1:
            startpoint = key
            break
    # startpoint = nums[0][0]
    res = [startpoint]
    nextvisit = dic[res[-1]]
    while True:
        if nextvisit[0] not in res:
            res.append(nextvisit[0])
        elif nextvisit[1] not in res:
            res.append(nextvisit[1])

        nextvisit = dic[res[-1]]
        if len(nextvisit) ==1:
            return res



# nums = [[3,5], [5,4]]
# nums = [[1,3],[7,6],[5,4],[4,3],[5,7]]
nums = [[3,5], [5,4], [4,2],[2,1]]
# nums =[[1,2],[2,1]]
print(recoverArr(nums))