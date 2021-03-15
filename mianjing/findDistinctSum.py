import random


def findDistinctSum(matrix, k):
    def prefixsum(matrix):
        m,n = len(matrix),len(matrix[0])
        newmatrix = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for i in range(m):
            for j in range(n):
                newmatrix[i+1][j+1] = matrix[i][j] +newmatrix[i][j+1] + newmatrix[i+1][j] - newmatrix[i][j]

        return newmatrix
    m, n = len(matrix),len(matrix[0])
    if k > min(m,n):
        return -1
    prefix = prefixsum((matrix))

    maxsum = -float('inf')
    max_i = 0
    max_j=0
    for i in range(k,m+1):
        for j in range(k,n+1):
            newsum = prefix[i][j]+prefix[i-k][j-k] - prefix[i][j-k] - prefix[i-k][j]
            if newsum > maxsum:
                maxsum = newsum
                max_i = i
                max_j = j

    print(max_i-1,max_j-1)
    res = []
    for i in range(max_i+1-k,max_i+1):
        for j in range(max_j+1-k,max_j+1):
            res.append(matrix[i-1][j-1])

    return res






m = 4
n = 5
k = 3
matrix = [[random.randint(1,10) for _ in range(n)] for _ in range(m)]
for r in matrix:
    print(r)
print(findDistinctSum(matrix,k))

