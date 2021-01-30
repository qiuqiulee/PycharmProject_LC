import heapq
def minimumEffortPath(heights):
    m, n = len(heights), len(heights[0])
    dist = [[float('inf')] * n for _ in range(m)]
    minHeap = [(0, 0, 0)]  # distance, row, col
    DIR = [0, 1, 0, -1, 0]
    while minHeap:
        d, r, c = heapq.heappop(minHeap)
        if d > dist[r][c]: continue
        if r == m - 1 and c == n - 1:
            return d  # Reach to bottom right
        for i in range(4):
            nr, nc = r + DIR[i], c + DIR[i + 1]
            if 0 <= nr < m and 0 <= nc < n:
                newDist = max(d, abs(heights[nr][nc] - heights[r][c]))
                if dist[nr][nc] > newDist:
                    dist[nr][nc] = newDist
                    heapq.heappush(minHeap, (dist[nr][nc], nr, nc))

heights = [[1,2,2],[3,8,2],[5,3,5]]
print(minimumEffortPath(heights))