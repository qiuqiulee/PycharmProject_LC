secret = "1123"
guess ="0111"
n = len(secret)
a = 0
b = 0
sel = []
gul = []
for i in range(n):
    if secret[i] == guess[i]:
        a += 1
    else:
        sel.append(secret[i])
        gul.append(secret[i])
n = len(sel)
for i in range(n):
    if sel[i] in gul:
        b += 1
        gul.pop(gul.index(sel[i]))

print(a,b)