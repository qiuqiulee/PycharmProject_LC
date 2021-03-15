def isSubmatrixFull(matrix):
    NofCol = len(matrix[0])
    dic = {}
    for row in range(3):
        for col in range(3):
            dic[matrix[row][col]] = dic.get(matrix[row][col],0)+1
    j =3
    res = []
    res.append(len(dic) ==9)
    while j<NofCol:
        for i in range(3):
            dic[matrix[i][j]] = dic.get(matrix[i][j], 0) + 1
            dic[matrix[i][j-3]] -= 1
            if dic[matrix[i][j-3]] ==0:
                del dic[matrix[i][j-3]]
        res.append(len(dic) ==9)
        j+=1
    return res










numbers = [[1, 2, 3, 2, 5, 7],
           [4, 5, 6, 1, 7, 6],
           [7, 8, 9, 4, 8, 3]]
a =[[1,2,3],[4,5,6],[7,8,6]]
print(isSubmatrixFull(a))