def shunzi(hand,W):

    l = len(hand)

    dic ={}
    for i in range(l):
        if hand[i] not in dic:
            dic[hand[i]] = 1
        else:
            dic[hand[i]] +=1
    dicls=sorted(dic)
    tpdic = {}
    for ind in dicls:
        tpdic[ind] = dic[ind]
    dic = tpdic
    while dicls:
        for i in range(W):
            a = dicls[0]
            if a+i not in dic:
                return False
            if dic[a+i] < 0:
                return False

            dic[a+i] -=1
            if dic[a+i] ==0:
                del dic[a+i]
        dicls =list(dic.keys())
    return True
hand = [1,2,3,6,2,3,4,7,8]
W = 3
print(shunzi(hand,W))
