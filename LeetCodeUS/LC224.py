s = "- (3 + (4 + 5))"

res, num, sign, stack = 0, 0, 1, []
for ss in s:
    if ss.isdigit():
        num = num * 10 + int(ss)
    elif ss in '+-':
        res += sign * num
        num = 0
        sign = -1 if ss == '-' else 1
    elif ss == '(':
        stack.append(res)
        stack.append(sign)
        res = 0
        sign = 1
    elif ss ==')':
        res += sign * num
        if stack:
            res *= stack.pop()
        if stack:
            res += stack.pop()
        num = 0
print(res+sign*num)