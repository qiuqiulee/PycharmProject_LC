n =3
dirc = [[0,1],[1,0],[0,-1],[-1,0]]
res= [[0 for _ in range(n)] for _  in range(n)]
dx  = 0
i = 1
x=0
y=-1

while i <n**2+1 :
    if 0<=x+dirc[dx][0]<n and 0<=y+dirc[dx][1]<n and res[x+dirc[dx][0]][y+dirc[dx][1]]==0:
        res[x+dirc[dx][0]][y+dirc[dx][1]] =i
        x = x+dirc[dx][0]
        y = y+dirc[dx][1]
    else:
        dx = (dx+1)%4
        res[x+dirc[dx][0]][y+dirc[dx][1]] =i
        x = x+dirc[dx][0]
        y = y+dirc[dx][1]
    i+=1
print(res)