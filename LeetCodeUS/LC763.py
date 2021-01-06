S = "ababcbacadefegdehijhklij"
uniqs =''
dic = {}
n = len(S)
for i in range(n):
    if S[i] in dic:
        if len(dic[S[i]])<2:
            dic[S[i]].append(i)
        else:
            dic[S[i]][1] = i
    else:
        uniqs+=S[i]
        dic[S[i]] = [i]
for item in dic:
    if len(dic[item]) < 2:
        dic[item].append(dic[item][0])

print(dic)
print(uniqs)
j = 0
anchor = 0
ans = []
for i in range(n):
    j = max(j,dic[S[i]][1])
    if i == j:
        ans.append(i-anchor+1)
        anchor = i +1
print(ans)


