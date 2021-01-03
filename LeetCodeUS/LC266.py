def canPermutePalindrome(s: str) -> bool:
    n = len(s)
    dic = {}
    for c in s:
        if c in dic:
            dic[c] += 1
        else:
            dic[c] = 1
    flg = 0
    for item in dic:
        if dic[item]%2 == 1:
            flg+=1
        if flg>1:
            return False
    return True
print(canPermutePalindrome('code'))