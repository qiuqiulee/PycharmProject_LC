def exist(board, word):
    def dfs(x, y, flg):
        if flg == len(word) - 1:
            return True
        visited[x][y] = 1
        for d in range(4):
            nx = x + dirc[d]
            ny = y + dirc[d + 1]
            if 0 <= nx < m and 0 <= ny < n and visited[nx][ny] == 0 and board[nx][ny] == word[flg + 1] and dfs(nx, ny, flg + 1):
                    return True
        visited[x][y] = 0



    m, n = len(board), len(board[0])
    dirc = [0, 1, 0, -1, 0]
    if len(word) > m * n:
        return False
    for i in range(m):
        for j in range(n):
            if board[i][j] == word[0]:
                visited = [[0 for _ in range(n)] for _ in range(m)]
                if dfs(i, j, 0):
                    return True
    return False

b =[["C","A","A"],
    ["A","A","A"],
    ["B","C","D"]]
w = "AABB"
print(exist(b,w))