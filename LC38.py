def cr(s):
    l=len(s)

    loc= 1
    res=''
    ct = 1
    while loc <l:
        if s[loc] == s[loc-1]:
            ct+=1
            loc+=1
        else:
            res += str(ct)+s[loc-1]
            ct = 1
            loc+=1
    res += str(ct)+s[loc-1]
    return res

ls = [' ','1']
pr ='1'
for i in range(29):
    nx = cr(pr)
    ls.append(nx)
    pr = nx

print(ls)

