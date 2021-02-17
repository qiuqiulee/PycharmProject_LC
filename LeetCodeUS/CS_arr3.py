def rotateImage(a):
    m = len(a)
    print(a)
    for i in range(m):
        for j in range(m):
            temp = a[i][j]
            a[i][j] = a[j][i]
            a[j][i] = temp
    print(a)
    for i in range(m):
        for j in range(m // 2):
            a[i][j], a[i][m - j - 1] = a[i][m - j - 1], a[i][j]
    return a


print(rotateImage([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]]))
