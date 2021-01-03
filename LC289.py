def ctlv(i, j):
    nl = 0
    for dx, dy in dirc:
        if 0 <= i + dx < m and 0 <= j + dy < n:
            if board[i + dx][j + dy] == 1:
                nl += 1
    return nl

board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
dirc = [[1, 0], [-1, 0], [1, 1], [1, -1], [0, 1], [0, -1], [-1, 1], [-1, -1], ]
m = len(board)
n = len(board[0])
nxb = [[0 for _ in range(n)] for _ in range(m)]
for x in range(m):
    for y in range(n):
        if board[x][y] == 1:
            if ctlv(x, y) < 2:
                nxb[x][y] = 0
            elif ctlv(x, y) < 4:
                nxb[x][y] = 1
            else:
                nxb[x][y] = 0
        elif ctlv(x, y) == 3:
            nxb[x][y] = 1
print(nxb)