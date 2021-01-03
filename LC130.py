
board =[["X","O","X","X"],["O","X","O","X"],["X","O","X","O"],["O","X","O","X"]]


m = len(board)
n = len(board[0])
sc = []
op = [["X" for _ in range(n)] for _ in range(m)]
for i in range(1, n - 1):
    if board[0][i] == "O":
        sc.append([0, i])
    if board[m - 1][i] == "O":
        sc.append([m - 1, i])
for j in range(1, m - 1):
    if board[j][0] == "O":
        sc.append([j, 0])
    if board[m - 1][i] == "O":
        sc.append([j, n - 1])
while sc:
    pt = sc.pop(0)
    op[pt[0]][pt[1]] = "O"
    if 0 <= pt[0] + 1 < m and board[pt[0] + 1][pt[1]] == "O" and op[pt[0] + 1][pt[1]] == "X":
        sc.append([pt[0] + 1, pt[1]])
    if 0 <= pt[0] - 1 < m and board[pt[0] - 1][pt[1]] == "O" and op[pt[0] - 1][pt[1]] == "X":
        sc.append([pt[0] - 1, pt[1]])
    if 0 <= pt[1] + 1 < n and board[pt[0]][pt[1] + 1] == "O" and op[pt[0]][pt[1]+1] == "X":
        sc.append([pt[0], pt[1] + 1])
    if 0 <= pt[1] - 1 < n and board[pt[0]][pt[1] - 1] == "O" and op[pt[0]][pt[1]-1] == "X":
        sc.append([pt[0], pt[1] - 1])

print(op)
