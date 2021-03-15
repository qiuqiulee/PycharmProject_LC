# https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=677778&ctid=231929
# 输入是(m,n,figures) 输出一个m*n的矩阵
# 给了5个图形，编号1，2，3，4，5 具体的形状记不太清，画了个大概，贴在图1
# figures是一列图形的编号
# 然后要求往m*n的全0矩阵里按照figures的顺序塞图形，位置优先往上，其次优先往左
# (直接按照for i in range(n): for j in range(m)搜索看能不能塞下就可以)，
# 找到能塞下的位置，把对应的格子的数改成i（i表示第i个图形）
# 例如 m=5,n=5, figures=[1,3,2,5], 输出的结果贴在图2