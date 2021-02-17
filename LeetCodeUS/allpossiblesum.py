def possibleSums(coins, quantity):
    m = len(quantity)
    dic= {}
    dic[0] = 1
    for i in range(m):
        pss = list(dic.keys())
        for ps in pss:
            for j in range(1,quantity[i]+1):
                if ps+j*coins[i] not in dic:
                    dic[ps+j*coins[i]] = 1

    for c, q in zip(coins, quantity):
        print(c,q)
    return len(dic)-1

coins = [10,50,100]
quantity = [1,2,1]

print(possibleSums(coins,quantity))