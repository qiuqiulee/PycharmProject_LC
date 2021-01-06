cell = [0,1,0,1,1,0,0,1]

recr = []
tpcell = cell[:]
for j in range(1, len(cell) - 1):
    if cell[j - 1] == cell[j + 1]:
        tpcell[j] = 1
    else:
        tpcell[j] = 0
tpcell[0] = 0
tpcell[-1] = 0
cell = tpcell[:]
recr.append(cell)
tp = []
while tp != recr[0]:
    tpcell = cell[:]
    for j in range(1, len(cell) - 1):
        if cell[j - 1] == cell[j + 1]:
            tpcell[j] = 1
        else:
            tpcell[j] = 0
    tpcell[0] = 0
    tpcell[-1] = 0
    cell = tpcell[:]
    recr.append(cell)
    tp = cell[:]

print(recr)
