def findDiagonalOrder(matrix):
    if not matrix:
        return []
    m = len(matrix)
    n = len(matrix[0])

    dic = {}
    for i in range(m):
        for j in range(n):
            if i - j not in dic:
                dic[i - j] = [matrix[i][j]]
            else:
                dic[i - j].append(matrix[i][j])
    res = []

    for key in sorted(dic):
        print(key)
        if key % 2 == 0:
            res += dic[key][::-1]
        else:
            res += dic[key]
    return res
matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
print(findDiagonalOrder(matrix))