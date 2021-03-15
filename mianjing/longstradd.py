s = "12378321927391"
k = 3
# res = ''
# while len(s)>k:
#     pieces = len(s) //k
#     remine = len(s) % k
#     if remine != 0:
#         addzero = k-remine
#         s = s[:pieces*k] + '0'* addzero +s[pieces*k:]
#         pieces = len(s) // k
#     m = k
#     carry = 0
#     new_s = ''
#     while m>0 or carry!=0:
#         tempsum = 0
#         if m >0:
#             for n in range(pieces):
#                 tempsum += int(s[n*k+m-1])
#         tempsum += carry
#         new_s = str(tempsum%10) + new_s
#         carry = tempsum //10
#         m-=1
#     s = new_s
#     print(s)
# print(s)

pieces = len(s) //k
remine = len(s) % k
if remine != 0:
    addzero = k-remine
    s = s[:pieces*k] + '0'* addzero +s[pieces*k:]
    pieces = len(s) // k
print(s)
temlist = [0 for _ in range(k)]
m = len(s)
for i in range(m):
    temlist[i%3] += int(s[i])

print(temlist)




