def closeword(i, j):
    flg = 0
    if len(wordList[i]) != len(beginWord) or len(wordList[j]) != len(beginWord):
        return 0
    for chi, chj in zip(wordList[i], wordList[j]):
        if chi != chj:
            flg += 1
            if flg > 1:
                return 0
    return 1


def backt(loc, visit, vistlist):
    if sum(visit) <= m and wordList[loc] == endWord:
        print(vistlist)
        op = vistlist[:]
        res.append(op)
    elif sum(visit)<=m:
        # vistlist.append(loc)
        # visit[loc] = 1
        for j in range(m):
            if visit[j] == 0 and matrix[loc][j] == 1:
                visit[j] = 1
                vistlist.append(j)
                backt(j, visit, vistlist)
                visit[j] = 0
                vistlist.pop(-1)


beginWord = "hot"
endWord = "dog"
wordList = ["hot", "cog", "dog", "tot", "hog", "hop", "pot", "dot"]
#
# beginWord ="qa"
# endWord = "sq"
# wordList = ["si", "go", "se", "cm", "so", "ph", "mt", "db", "mb", "sb", "kr", "ln", "tm", "le", "av", "sm", "ar", "ci", "ca", "br",
#  "ti", "ba", "to", "ra", "fa", "yo", "ow", "sn", "ya", "cr", "po", "fe", "ho", "ma", "re", "or", "rn", "au", "ur", "rh",
#  "sr", "tc", "lt", "lo", "as", "fr", "nb", "yb", "if", "pb", "ge", "th", "pm", "rb", "sh", "co", "ga", "li", "ha", "hz",
#  "no", "bi", "di", "hi", "qa", "pi", "os", "uh", "wm", "an", "me", "mo", "na", "la", "st", "er", "sc", "ne", "mn", "mi",
#  "am", "ex", "pt", "io", "be", "fm", "ta", "tb", "ni", "mr", "pa", "he", "lr", "sq", "ye"]

wordList = [beginWord] + wordList
m = len(wordList)
matrix = [[0 for _ in range(m)] for _ in range(m)]

for i in range(m - 1):
    for j in range(i + 1, m):
        matrix[i][j] = closeword(i, j)
        matrix[j][i] = closeword(i, j)
for i in range(m):
    matrix[i][0] = 0
res = []
for i in range(m):
    if matrix[0][i] == 1:
        visited = [0 for _ in range(m)]
        visited[0] = 1
        visited[i] = 1
        backt(i, visited, [0, i])

# print(matrix)

print(res)
#

shortest = m
indexlist = []

for wordlist in res:
    if wordlist and len(wordlist) < shortest:
        shortest = len(wordlist)
        indexlist = wordlist[:]

print(indexlist)
print(wordList)
