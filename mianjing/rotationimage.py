def clock(grid):
    m = len(grid)
    if m == 1:
        return grid
    for i in range(m-1):
        for j in range(i+1,m):
            grid[i][j], grid[j][i]= grid[j][i],grid[i][j]
    for i in range(m):
        for j in range(m//2):
            grid[i][j],grid[i][m-1-j] = grid[i][m-1-j],grid[i][j]

    return grid

def clock_w_a(grid):
    m = len(grid)
    if m == 1:
        return grid

    return grid

def anticlock(grid):
    m = len(grid)
    if m ==1:
        return grid
    for i in range(m-1):
        for j in range(m-1-i):
            grid[i][j], grid[m-1-j][m-1-i] =grid[m-1-j][m-1-i] , grid[i][j]
    for i in range(m):
        for j in range(m//2):
            grid[i][j],grid[i][m-1-j] = grid[i][m-1-j],grid[i][j]

    return grid

def anticolock_w_a(grid):
    m = len(grid)
    if m == 1:
        return grid

    return grid

def upside(grid):
    m = len(grid)
    if m == 1:
        return grid
    for i in range(m//2):
        for j in range(m):
            grid[i][j],grid[m-1-i][m-1-j] = grid[m-1-i][m-1-j],grid[i][j]
    if m%2 == 1:
        for j in range(m//2):
            grid[m//2][j], grid[m//2][m - 1 - j] = grid[m//2][m - 1 - j], grid[m//2][j]


    return grid
g1 = [1]
g2 = [[1,2],[3,4]]
g3 = [[1,2,3],[4,5,6],[7,8,9]]
g4 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
g5 = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]

for row in clock(g1):
    print(row)
for row in clock(g2):
    print(row)
for row in clock(g3):
    print(row)
for row in clock(g4):
    print(row)
for row in clock(g5):
    print(row)


# for row in clock_w_a(g1):
#     print(row)
# for row in clock_w_a(g2):
#     print(row)
# for row in clock_w_a(g3):
#     print(row)
# for row in clock_w_a(g4):
#     print(row)
# for row in clock_w_a(g5):
#     print(row)
#
for row in anticlock(g1):
    print(row)
for row in anticlock(g2):
    print(row)
for row in anticlock(g3):
    print(row)
for row in anticlock(g4):
    print(row)
for row in anticlock(g5):
    print(row)


# for row in anticolock_w_a(g1):
#     print(row)
# for row in anticolock_w_a(g2):
#     print(row)
# for row in anticolock_w_a(g3):
#     print(row)
# for row in anticolock_w_a(g4):
#     print(row)
# for row in anticolock_w_a(g5):
#     print(row)
#
for row in upside(g1):
    print(row)
for row in upside(g2):
    print(row)
for row in upside(g3):
    print(row)
for row in upside(g4):
    print(row)
for row in upside(g5):
    print(row)