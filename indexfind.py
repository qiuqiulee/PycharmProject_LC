dic = {20:['De'],
       21:['So','NI','De'],
       22:['De','So'],
       23:['De','So'],
       26:['De','So','NI','CW'],
       27:['De','So'],
       38:['De'],
       37:['De','So'],
       40:['De','So'],
       38:['De','So'],
       33:['De','CC','NI'],
       32:['NI'],
       31:['De','So','NI','CW'],
       25:['De']}
odic = {}
keys = dic.keys()
for k in keys:
    for ele in dic[k]:
        if ele not in odic:
            odic[ele] = [k]
        else:
            odic[ele].append(k)

keys = odic.keys()
for k in keys:
    odic[k].sort()

print(odic)