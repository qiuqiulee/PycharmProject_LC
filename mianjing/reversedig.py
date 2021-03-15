# reverse pair digits
# 就是一个int从左往右每两个digit调换一下，比如输入是12345，输出就是21435
# 我遇到了一个很迷的情况，因为要把int转换成char array才能两两调换，但是用了Integer.toString().toCharArray()，看到了莫名其妙的error message，而且问题在main函数里，感觉不是我的锅

num = 123456
s_arr = list(str(num))
m = len(s_arr)
i = 0
while i+1<m:
    s_arr[i],s_arr[i+1] = s_arr[i+1],s_arr[i]
    i+=2
print(int(''.join(s_arr)))