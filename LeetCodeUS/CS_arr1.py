def firstDuplicate(a):
    dic ={}
    for num in a:
        if num not in dic:
            dic[num] = 1
        else:
            return num
    retrun -1

print(firstDuplicate(([5,5,5,5,5,])))