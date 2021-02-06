def numMatchingSubseq(S,words) -> int:
    dic = {}
    m = len(S)
    res = 0
    for i in range(m):
        if S[i] in dic:
            dic[S[i]].append(i)
        else:
            dic[S[i]] = [i]
    for w in words:
        n = len(w)
        i = 0
        start = 0
        while i < n:
            if w[i] not in dic:
                break
            elif dic[w[i]][-1] < start:
                break
            else:
                j = 0
                while dic[w[i]] and dic[w[i]][j] < start:
                    j+=1
                if j >= len(dic[w[i]]):
                    break
                else:
                    start = dic[w[i]][j] + 1
            i += 1
        if i == n:
            res += 1
    return res

print(numMatchingSubseq("abcde",["a","bbbbbb","acd","ace"]))

print(numMatchingSubseq("qlhxagxdqh",["qlhxagxdq","qlhxagxdq","lhyiftwtut","yfzwraahab"]))
print(numMatchingSubseq("qlhxagxdqh",["qlhxagxdq","qlhxagxdq"]))
print(numMatchingSubseq("qlhxagxdqh",["lhyiftwtut","yfzwraahab"]))