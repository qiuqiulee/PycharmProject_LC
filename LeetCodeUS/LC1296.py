from collections import Counter
import heapq
def isPossibleDivide(nums, k) :
    heap = []
    m = len(nums)
    if m%k != 0:
        return False
    d = Counter(nums)
    for n in d:
        heapq.heappush(heap,[n,d[n]])
    print(heap)

    while heap:
        temp = []
        sml,freq = heapq.heappop(heap)
        for i in range(1,k):
            if not heap:
                return False
            n2,freq2 = heapq.heappop(heap)
            if freq2 < freq or n2-i !=sml:
                return False
            elif freq2 > freq:
                temp.append([n2,freq2-freq])
        while temp:
            x,f = temp.pop()
            heapq.heappush(heap, [x, f])
    return True


nums =[1,1,2,2,3,3]

k = 2
print(isPossibleDivide(nums,k))