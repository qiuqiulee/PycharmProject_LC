cells = [0,1,0,1,1,0,0,1]
day = [cells]
for w in range(10):
    ncell = [0] * 8
    for i in range(1,7):
        ncell[i] = 1 if cells[i-1]==cells[i+1] else 0
    lb = cells[:]
    cells = ncell[:]
    # print(cells)
dy =0
rec = []
while cells != lb:
    rec.append(cells)
    ncell = [0] * 8
    for i in range(1,7):
        ncell[i] = 1 if cells[i-1]==cells[i+1] else 0
    cells = ncell[:]
rec.append(cells)
print(rec)