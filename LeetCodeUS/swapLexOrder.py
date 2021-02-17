# def swapLexOrder(str, pairs):
#     dic= {}
#     m= len(str)
#     for i in range(m):
#         dic[i] = [i]
#
#     for i, j in pairs:
#
#         if i-1 not in dic:
#             dic[i-1] = [j-1]
#         else:
#             dic[i-1].append(j-1)
#
#         if j-1 not in dic:
#             dic[j-1] = [i-1]
#         else:
#             dic[j-1].append(i-1)
#
#     for i in dic: #dic[1] = [4]
#         for j in dic[i]:
#             if j>i:
#                 for k in dic[j]:
#                     if k not in dic[i]:
#                         dic[i].append(k)
#     #
#     res = ['0' for _ in range(m)]
#     visited = ()
#     for ch in dic:
#         if len(dic[ch]) == 1:
#             res[ch] = str[ch]
#             visited.add(ch)
#     for i in range(m):
#         if i not in visited:
#             temp = []
#             for j in dic[i]:
#                 if j not in visited:
#                     temp.append()
#     print(res)
#     print(dic)
#
def build_permitted_subs(pairs):
    perm = []

    for a, b in pairs:
        merged = False
        for ind, sub_perm in enumerate(perm):
            if a in sub_perm or b in sub_perm:
                sub_perm.add(a)
                sub_perm.add(b)
                merged = True
                break

        else:
            perm.append(set([a, b]))

        if merged:
            for merge_perm_ind in reversed(range(ind + 1, len(perm))):
                if perm[merge_perm_ind] & sub_perm:
                    sub_perm.update(perm[merge_perm_ind])
                    perm.pop(merge_perm_ind)

    return list(map(sorted, perm))

def swap_lex_order(swap_str, _pairs):

    pairs = [[a - 1, b - 1] for a, b in _pairs]
    out = list(swap_str)

    perm = build_permitted_subs(pairs)

    for sub_perm in perm:
        sorted_subset = sorted(sub_perm, key=lambda w: swap_str[w], reverse=True)

        for sort, targ in zip(sorted_subset, sub_perm):
            out[targ] = swap_str[sort]

    return "".join(out)

print(swap_lex_order("dznsxamwoj", [[1, 2], [3, 4], [6, 5], [8, 10]]))
# print(swap_lex_order("abdc", [[1, 4], [3, 4]]))
# print(swap_lex_order("acxrabdz",[[1,3], [6,8], [3,8], [2,7]]))


