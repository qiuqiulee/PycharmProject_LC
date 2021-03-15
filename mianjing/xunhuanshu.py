# 2) 给定一个数组，判断是不是[1...n]或[n...1]的数字移位结果，例如[n,1,2...n-1]是[1...n]的移位结果
import random
nums = [random.randint(1,10) for _ in range(10)]
n1= [7, 10, 9, 5, 4, 7, 2, 5, 3, 8]
c2= [8, 3, 5, 2, 7, 4, 5, 9, 10, 7]
startnum = []
for ind,n in enumerate(c2):
    if n == 8:
        startnum.append(ind)
while startnum:
    newstart = startnum.pop()
    newlist =c2[newstart:] +c2[:newstart]
    print(newlist)
    newlist = c2[:newstart][::-1] + c2[newstart:][::-1]
    print(newlist)
# print(nums)