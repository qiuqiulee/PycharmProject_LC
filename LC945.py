def findm(lis, left, right,res):
    if left == right:
        return res,lis
    if left < right:
        if lis[left] < lis[left + 1]:
            findm(lis, left + 1, right,res)
        else:
            res = res + lis[left]+1-lis[left + 1]
            lis[left + 1] = lis[left]+1
            findm(lis, left + 1, right,res)
    return res,lis



A =[1,2,2,2,3,4]

res = 0
l = len(A)
for i in range(1,l):
    if A[i]<=A[i-1]:
        res += A[i-1]+1 - A[i]
        A[i] = A[i-1]+1

print(A,res)