def countSquares(matrix):
    def checksq(x, y, s):
        for dx in range(s+1):
            if matrix[x + s][y + dx] == 0 or matrix[x + dx][y + s] == 0:
                return False
        return True

    m, n = len(matrix), len(matrix[0])
    res = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1:
                size = 0
                while i + size < m and j + size < n and checksq(i, j, size):
                    size += 1
                res += size
                print(size,res)

    return res

countSquares([[0,1,1,1],[1,1,1,1],[0,1,1,1]])