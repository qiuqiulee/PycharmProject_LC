people = [[9,0],[7,0],[1,9],[3,0],[2,7],[5,3],[6,0],[3,4],[6,2],[5,2]]



# people = sorted(people, key=lambda x: (-x[0], x[1]))
# new_people = [people[0]]
# for i in people[1:]:
#     new_people.insert(i[1], i)
# print(new_people)

dic  = {}

for x in people:
    if x[0] not in dic:
        dic[x[0]] =[x[1]]
    else:
        dic[x[0]].append(x[1])

sk = list(dic.keys())
sk.sort(reverse = True)
res = []
for ele in sk:
    dic[ele].sort()
    for loc in dic[ele]:
        res.insert(loc,[ele, loc])
print(res)