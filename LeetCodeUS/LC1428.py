# a=[0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
a=[0,0,0,0]
i = 0
j = len(a)
while i<j:
    mid = (j+i) //2
    if a[mid] == 0:
        i = mid+1
    else:
        j = mid
w,x =[1,2]
print(i)
print(w,x)