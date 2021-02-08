s = "1+(2-(3+4))"

res, num, sign, stack = 0, 0, 1, []
for ss in s:
    if ss.isdigit():
        num = 10 * num + int(ss)
    elif ss in ["-", "+"]:
        res += sign * num
        num = 0
        sign = [-1, 1][ss == "+"]
    elif ss == "(":
        stack.append(res)
        stack.append(sign)
        sign, res = 1, 0
    elif ss == ")":
        res += sign * num
        res *= stack.pop()
        res += stack.pop()
        num = 0
print(res + num * sign)


res = 0
num = 0
sign = 1
stack =[]
for ss in s:
    if ss.isdigit():
        num = int(ss) + num * 10
    elif ss in ['+','-']:
        res += sign * num
        num = 0
        if ss == '+':
            sign = 1
        else:
            sign = -1
    
    elif ss =='(':
        stack.append(res)
        stack.append(sign)
        res = 0
        sign = 1
    else:
        res += sign * num
        res *= stack.pop()
        res += stack.pop()
        num =0
print(res+ sign*num)
            

