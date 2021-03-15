import collections

grid = [[1, 2, 3, 4, 5, 5, 6, 7, 5, 4],
        [1, 4, 5, 3, 4, 5, 4, 3, 4, 5],
        [4, 5, 6, 7, 1, 3, 4, 5, 6, 7]]

n = len(grid[0])
for i in range(n-3):
        templist = grid[0][i:i+3] + grid[1][i:i+3] + grid[2][i:i+3]
        print(collections.Counter(templist))
