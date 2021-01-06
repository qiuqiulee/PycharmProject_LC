def LC819(paragraph,banned):
    for c in "!?',;.":
        paragraph = paragraph.replace(c, " ")
    paragraph_list = paragraph.split(' ')
    dic = {}
    for word in paragraph_list:
        if word:
            if word.lower() in dic and word.lower() not in banned:
                dic[word.lower()] += 1
            elif word.lower() not in banned:
                dic[word.lower()] = 1
    if dic == {}:
        return ""
    candidate = list(dic.keys())
    freq = list(dic.values())
    indx_max = max(freq)

    return candidate[freq.index(indx_max)]
p = "Bob. hIt, baLl"
b = ["bob", "hit"]
print(LC819(p,b))