s = "010010"
m = len(s)
res = []

for i in range(m - 3):
    for j in range(i + 1, m - 2):
        for k in range(j + 1, m - 1):
            num1 = int(s[0:i + 1])
            num2 = int(s[i + 1:j + 1])
            num3 = int(s[j + 1:k + 1])
            num4 = int(s[k + 1:m])
            if 0 <= num1 <= 255 and 0 <= num2 <= 255 and 0 <= num3 <= 255 and 0 <= num4 <= 255 and (len(
                    str(num1)) == i + 1 or (num1 == 0 and i == 0)) and (
                    len(str(num2)) == j - i or (num2 == 0 and j - i == 1)) and (
                    len(str(num3)) == k - j or (num3 == 0 and k - j == 1)) and (len(
                str(num4)) == m - k - 1 or (num4 == 0 and m - k - 1 == 1)):
                res.append(s[0:i + 1] + "." + s[i + 1:j + 1] + "." + s[j + 1:k + 1] + "." + s[k + 1:m])
            else:
                continue
print(res)
