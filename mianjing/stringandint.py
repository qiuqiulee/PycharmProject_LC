# 输入是一个string和一个int array，int array里的所有元素的和等于string的长度。要求把string按照int array给拆成小的string。
# 然后对这些substring进行一些操作，最后像第一题那种调换顺序

s = 'abcdefg'
list = [1,2,4]

s_list = []
i = 0
while list:
    step = list.pop(0)
    s_list.append(s[i:i+step])
    i +=step
print(s_list)

