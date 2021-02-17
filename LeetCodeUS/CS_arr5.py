def isCryptSolution(crypt, solution):
    dic = {}
    for s in solution:
        dic[s[0]] = int(s[1])
    for word in crypt:
        if len(word) > 1 and dic[word[0]] == 0:
            return False
    if len(crypt[2]) - max(len(crypt[0]), len(crypt[1])) > 1 or len(crypt[2]) - max(len(crypt[0]), len(crypt[1])) < 0:
        return False

    m = len(crypt[2])
    add1 = [0 for _ in range(m)]
    len1 = len(crypt[0])
    for i in range(len1):
        add1[i] = dic[crypt[0][len1 - i - 1]]
    add2 = [0 for _ in range(m)]
    len2 = len(crypt[1])
    for i in range(len2):
        add2[i] = dic[crypt[1][len2 - i - 1]]
    res = [0 for _ in range(m)]
    for i in range(m):
        res[i] = dic[crypt[2][m - i - 1]]

    i = 0
    ten = 0
    while i < m:
        if (add1[i] + add2[i] + ten) % 10 == res[i]:
            ten = (add1[i] + add2[i] + ten) // 10
            i += 1
        else:
            return False
    return True

cr=["A",
 "B",
 "C"]
so=[["A","5"],
 ["B","6"],
 ["C","1"]]
print(isCryptSolution(cr,so))