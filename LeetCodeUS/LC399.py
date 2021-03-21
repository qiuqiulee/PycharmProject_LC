

equations = [["a", "b"], ["a", "c"], ["a", "d"], ["a", "e"], ["a", "f"], ["a", "g"], ["a", "h"], ["a", "i"], ["a", "j"],
             ["a", "k"], ["a", "l"], ["a", "aa"], ["a", "aaa"], ["a", "aaaa"], ["a", "aaaaa"], ["a", "bb"],
             ["a", "bbb"], ["a", "ff"]]
values = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 1.0, 1.0, 1.0, 1.0, 1.0, 3.0, 5.0]
q = [["d", "f"], ["e", "g"], ["e", "k"], ["h", "a"], ["aaa", "k"], ["aaa", "i"], ["aa", "e"], ["aaa", "aa"],
     ["aaa", "ff"], ["bbb", "bb"], ["bb", "h"], ["bb", "i"], ["bb", "k"], ["aaa", "k"], ["k", "l"], ["x", "k"],
     ["l", "ll"]]


dic = {}
m = len(equations)
for i in range(m):
    if equations[i][0] not in dic:
        dic[equations[i][0]] = {}
        dic[equations[i][0]][equations[i][0]] = 1
    if equations[i][1] not in dic:
        dic[equations[i][1]] = {}
        dic[equations[i][1]][equations[i][1]] = 1
    dic[equations[i][0]][equations[i][1]] = values[i]
    dic[equations[i][1]][equations[i][0]] = 1 / values[i]

print(dic)

for key in dic:
    seen = set()
    seen.add(key)
    nextvisit = []
    for ele in dic[key].keys():
        if ele not in seen:
            nextvisit.append(ele)
    temp = []
    while nextvisit:
        for ele in nextvisit:
            ratio = dic[key][ele]
            seen.add(ele)
            for ele2 in dic[ele]:
                if ele2 not in seen:
                    dic[key][ele2] = ratio * dic[ele][ele2]
                    temp.append(ele2)
        nextvisit = temp
        temp = []
print(dic['aaa'])



