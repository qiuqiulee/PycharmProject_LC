#
# def quicksort(arr,i,j):
#     if i < j:
#         q = partsort(arr,i,j)
#         quicksort(arr,i,q-1)
#         quicksort(arr,q+1,j)
#     return arr
#
# def partsort(arr,left,right):
#     pivot = left
#     index = pivot +1
#     i = index
#     while i <= right:
#         if arr[i] < arr[pivot]:
#             arr[i],arr[index] = arr[index],arr[i]
#             index +=1
#         i+=1
#     arr[pivot], arr[index-1] = arr[index-1], arr[pivot]
#     return index-1
#
# arr = [1,5,3,23,4,5,43,32,34,4,5]
# print(quicksort(arr,0,len(arr)-1))

def qs(arr,i,j):
    if i<j:
        q= partsort(arr,i,j)
        qs(arr,i,q)
        qs(arr,q+1,j)
    return arr

def partsort(arr,left,right):
    pivot =  left
    index = pivot+1
    i = index
    while i<= right:
        if arr[pivot] > arr[i]:
            arr[i],arr[index]= arr[index],arr[i]
            index += 1
        i+=1

    arr[pivot],arr[index-1]= arr[index-1], arr[pivot]
    return index -1

arr= [432,3,4,2,3,54,5,3,2,4]
l = len(arr)
print(qs(arr,0,l-1))



















