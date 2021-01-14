def numRescueBoats(people, limit):
    run = 0
    m = len(people)
    dic = {}
    for i in range(m):
        if people[i] in dic:
            dic[people[i]] += 1
        else:
            dic[people[i]] = 1
    key = list(dic.keys())
    key.sort(reverse=True)
    while dic:
        for k in key:
            if dic and dic[k]:
                numofbig = dic[k]
                budy = limit - k
                while dic[k]>0 and budy > 0 and numofbig > 0:
                    if dic and budy in dic:
                        dic[budy] -= 1
                        numofbig -= 1
                        run += 1
                        dic[k] -= 1
                        if dic and dic[budy] == 0:
                            dic.pop(budy)
                        if dic and dic[k] ==0:
                            dic.pop(k)
                    elif budy - 1 > 0:
                        budy -= 1
                    else:
                        break
                if dic and dic[k]:
                    run += dic[k]
                    dic.pop(k)
    return runÒ
people = [3,5,3,4]
limit = 5
print(numRescueBoats(people,limit))