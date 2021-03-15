arr = [0,1,0,1,0,0,0,0,0,0,1,0,1,1,0,0,0,1,0,1,0,1,0]
m = len(arr)
i = 0
j  = 0
k = 3
# while i<m and j<m:
# #     while i<m and arr[i] == 1:
# #         i+=1
# #     j = i
# #     while j-i <=3 and j<m and arr[j]==0:
# #         j+=1
# #     if j<m and arr[j] == 1 and j-i<=3:
# #         i=j
# #         continue
# #     else:
# #         print(i,j)
# #
# #         i+=1

while i<m:
    if arr[i] == 1:
        i+=1
    else:
        j=i+1
        while j-i<3 and j<m and arr[j] == 0:
            j+=1
            if j-i ==3:
                print(i,j)
                i+=1
        i+=1