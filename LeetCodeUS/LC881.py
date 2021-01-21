def numRescueBoats(people, limit) -> int:
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
                while k in dic and budy > 0 and numofbig > 0 :
                    if budy == k and dic[k] % 2 == 0:
                        run += dic[k] // 2
                        dic.pop(k)
                    elif budy == k and dic[k] % 2 != 0:
                        run += dic[k] // 2 + 1
                        dic.pop(k)
                    if dic and budy in dic:
                        dic[budy] -= 1
                        numofbig -= 1
                        run += 1
                        dic[k] -= 1
                        if dic and dic[budy] == 0:
                            dic.pop(budy)
                        if dic and dic[k] ==0:
                            dic.pop(k)
                    elif budy - 1 >= 0:
                        budy -= 1
                    else:
                        break


                if dic and k in dic:
                    run += dic[k]
                    dic.pop(k)
    return run
people = [3,1,7]
limit = 7
print(numRescueBoats(people,limit))