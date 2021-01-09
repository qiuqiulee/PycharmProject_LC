

def check(word1,word2):
    m=0
    n=0
    for w in word1:
        m+=len(w)
    for w in word2:
        n+=len(w)

    if m != n:
        return False
    overlen = m
    m = len(word1)
    n = len(word2)

    i1 = 0
    j1 = 0
    i2 = 0
    j2 = 0
    passwd = 0
    while passwd<overlen:
        if word1[i1][j1] != word2[i2][j2]:
            return False
        j1+=1
        j2+=1
        if j1 == len(word1[i1]):
            j1 = 0
            i1 += 1
        if j2 == len(word2[i2]):
            j2 = 0
            i2 += 1

        passwd +=1
    return True


word1 = ["ab", "c"]
word2 = ["a", "bc"]

print(check(word1,word2))