# 给一个n*n矩阵，把最外一圈的数字从小到大排序，再放回最外一圈（从左上角开始）。然后再第二靠外的一圈，
import random

m = 10
grid = [[random.randint(0, 10) for _ in range(m)] for _ in range(m)]
print(grid)
circle = m // 2
for step in range(circle):
    edge_len = m - 1 - 2 * step
    sorting = [0] * 4 * edge_len
    for i in range(edge_len):
        sorting[i] = grid[step][step + i]
        sorting[edge_len * 1 + i] = grid[step + i][step + edge_len]
        sorting[edge_len * 2 + i] = grid[step + edge_len][step + edge_len - i]
        sorting[edge_len * 3 + i] = grid[step + edge_len - i][step]
    print(sorting)
    sorting.sort()
    print(sorting)
    for i in range(edge_len):
        grid[step][step + i] = sorting[i]
        grid[step + i][step + edge_len] = sorting[edge_len * 1 + i]
        grid[step + edge_len][step + edge_len - i] =sorting[edge_len * 2 + i]
        grid[step + edge_len - i][step] =  sorting[edge_len * 3 + i]

print(grid)


def transMatrix(matrix):
    if not matrix:
        return []
    m = len(matrix)
    if m < 2:
        return matrix
    step = m // 2
    for i in range(step):
        singleLength = m - 1 - 2 * step
        arr = [0 for _ in range(4 * singleLength)]
               for j in range(singleLength):
        arr[j] = matrix[i][i + j]
        arr[j + singleLenght * 1] = matrix[i + j][singleLength + i]
        arr[j + singleLenght * 2] = matrix[singleLength + i][singleLength + i - j]
        arr[j + singleLenght * 3] = matrix[singleLength + i - j][i]
        arr.sort()
        print(arr)
        for j in range(singleLength):
            matrix[i][i + j] = arr[j]
        matrix[i + j][singleLength + i] = arr[j + singleLenght * 1]
        matrix[singleLength + i][singleLength + i - j] = arr[j + singleLenght * 2]
        matrix[singleLength + i - j][i] = arr[j + singleLenght * 3]
