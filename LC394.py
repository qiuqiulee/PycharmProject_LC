def decodeString(s):
        stack = []

        for c in s:
            if c != "]":
                stack.append(c)
            else:
                tmp = ""
                while stack[-1] != "[":
                    tmp = stack.pop(-1) + tmp
                stack.pop(-1)
                times = ""
                while stack and stack[-1].isdigit():
                    times = stack.pop(-1) + times
                times = int(times)

                # tmp = "".join(tmp for _ in range(times))
                tmp = tmp * times
                for t in tmp:
                    stack.append(t)
        return "".join(stack)

print(decodeString("3[a]2[bc]"))