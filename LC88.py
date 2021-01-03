nums1=[2,0]
m=1
nums2=[1]
n=1


l = m+n -1
i = m -1
j = n -1
while l>0:
    if i == 0 and j ==0:
        nums1[0] == min(nums1[i],nums2[j])
        nums1[1] == max(nums1[i], nums2[j])
    elif i ==0:
        nums1[l] = nums2[j]
        j-=1
    elif j == 0:
        nums1[l] = nums1[i]
        i-=1
    elif nums1[i] >= nums2[j]:
        nums1[l] = nums1[i]
        i-=1
    else: # nums1[i] < nums[j]:
        nums1[l] = nums2[j]
        j-=1
    l-=1

print(nums1)

