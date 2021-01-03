buildings =[[2,9,10]]
l = len(buildings)
lfs =[]
rts =[]
res =[]
for b in buildings:
    lfs.append(b[0])
    rts.append(b[1])

buildings2d = [0]* (max(rts)+1)

for b in buildings:
    for xi in range(b[0],b[1]+1):
        buildings2d[xi] = max(buildings2d[xi],b[2])
i = 0
temp = 0

for i in range(len(buildings2d)-1):
    if buildings2d[i] != buildings2d[i+1]:
        if len(res) and res[-1][1] > buildings2d[i+1]:
            res.append([i, buildings2d[i + 1]])
        else:
            res.append([i+1,buildings2d[i+1]])
res.append([max(rts),0])
print([[buildings[0][0],buildings[0][2]],[[buildings[0][1],buildings[0][2]]]
