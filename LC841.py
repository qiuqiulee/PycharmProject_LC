rooms = [[1],[2],[3],[]]
m = len(rooms)
checked = [False] * m
checked[0] = True
stack = [] + rooms[0]
while stack:
    ck = stack.pop()
    if checked[ck]:
        continue
    else:
        checked[ck] = 1
        stack += rooms[ck]
print(all(checked))