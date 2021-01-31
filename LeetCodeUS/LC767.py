import heapq
import collections
def reorganizeString(S):
    heap = []
    res =[]
    d = collections.Counter(S)
    for c in d:
        heapq.heappush(heap,(-d[c],c))
    m = len(S)
    res =[None] * m
    freq,chr = heapq.heappop(heap)
    freq = -freq
    if m%2 ==0:
        if freq >m/2:
            return ""
        else:
            for i in range(int(m/2)):
                if freq == 0:
                    freq, chr = heapq.heappop(heap)
                    freq = -freq
                res[i*2] = chr
                freq -=1
            for i in range(int(m/2)):
                if freq == 0:
                    freq, chr = heapq.heappop(heap)
                    freq = -freq
                res[i*2+1] = chr
                freq -=1
    else:
        if freq > (m+1)/2:
            return ""
        else:
            for i in range(int((m+1)/2)):
                if freq == 0:
                    freq, chr = heapq.heappop(heap)
                    freq = -freq
                res[i*2] = chr
                freq -=1
            for i in range(int((m-1)/2)):
                if freq == 0:
                    freq, chr = heapq.heappop(heap)
                    freq = -freq
                res[i*2+1] = chr
                freq -=1
    return ''.join(res)

S = 'aaaaabcdefd'
print(reorganizeString(S))

