nums =[1,2,-1,1,2,-1,1,2,-1]
k = 2
pre = 0
count = 0
dic = {0: 1}
for i in nums:
    pre += i
    if (pre - k) in dic:
        count += dic[pre - k]
    dic[pre] =  dic.get(pre,0) + 1

print(count)