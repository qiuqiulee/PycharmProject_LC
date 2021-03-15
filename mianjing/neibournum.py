nums = [[1,3],[7,6],[5,4],[4,3],[5,7]]
dic = {}
for i,j in nums:
    if i in dic:
        dic[i].append(j)
    else:
        dic[i] = [j]
    if j in dic:
        dic[j].append(i)
    else:
        dic[j] = [i]
m = len(dic)
res =[nums[0][0]]
nextvisit = dic[nums[0][0]][0]

for _ in range(m-1):
    res.append(nextvisit)
    nextvisit = dic[nextvisit][0] if res[-2]!=dic[nextvisit][0] else dic[nextvisit][1]



print(dic)
print(res)