combine =[
                [],
                [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], #1
                [1,2,4,6,8,10,12,14],#2
                [1,3,6,9,12,15],#3
                [1,2,4,8,12],#4
                [1,5,10,15],#5
                [1,2,3,6,12],#6
                [1,7,14],#7
                [1,2,4,8],#8
                [1,3,9],#9
                [1,2,5,10],#10
                [1,11],#11
                [1,2,3,4,6,12],#12
                [1,13],#13
                [1,2,7,14],#14
                [1,3,5,15],#15
        ]
#testnew
def bt(i,j,tp):
    if i == n+1:
        res_t = tp[:]
        res.append(res_t)
        return
    else:
        for k in range(j,len(combine[i])):
            if combine[i][k] not in tp and combine[i][k] <=n:
                tp.append(combine[i][k])
                bt(i+1,0,tp)
                tp.pop(-1)


res = []
n =8
bt(1,0,[])
print(len(res))