import heapq
import random

while True:
    m = 9
    a = [random.randint(0, 20) for _ in range(m)]
    b = [random.randint(0, 10) for _ in range(m)]


    aabbss = [abs(a[i]-b[i]) for i in range(m)]

    delta_list = []
    method2 = []
    for i in range(m):
        for j in range(m):
            # delta_list.append([abs(a[i]-b[j])+abs(a[j]-b[i])-abs(a[i]-b[i])-abs(a[j]-b[j]),i,j])
            heapq.heappush(delta_list, [abs(a[j] - b[i]) - abs(a[i] - b[i]), i, j])
            ttt = a[i]
            a[i] = a[j]
            tempabs = 0
            for w in range(m):
                tempabs += abs(a[w] - b[w])
            heapq.heappush(method2, [tempabs, i, j])
            a[i] = ttt



    if aabbss.index(max(aabbss)) not in [delta_list[0][1],delta_list[0][2]]:
        print(a)
        print(b)
        print(aabbss)
        print(max(aabbss), aabbss.index(max(aabbss)))
        print(delta_list)
        print(method2)
        break
