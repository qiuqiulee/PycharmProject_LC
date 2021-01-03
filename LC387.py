s = 'leecode'
dic= {}
reslis = []
dp =set()
for i in s:
    # if i not in dic:
    #     dic[i] = 1
    # else:
    #     dic[i]+=1
    if i not in reslis and i not in dp:
        reslis.append(i)
    elif i in reslis:
        ind = reslis.index(i)
        reslis.pop(ind)
        dp.add(i)



print(reslis)