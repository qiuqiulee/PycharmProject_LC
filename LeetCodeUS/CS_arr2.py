from collections import Counter

def firstNotRepeatingCharacter(s):
    dic = Counter(s)
    viewed = set()
    for ch in s:
        if ch not in viewed:
            viewed.add(ch)
            if dic[ch] ==1:
                return ch
    return -1

print(firstNotRepeatingCharacter('abcabc'))