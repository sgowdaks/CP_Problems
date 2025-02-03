#Dijkstra’s Algorithm

import heapq

v = 9
arr = [(0, 1, 4), (0, 7, 8), (1, 2, 8), (1, 7, 11), (2, 3, 7), (2, 8, 2), (2, 5, 4), (3, 4, 9), (3, 5, 14), (4, 5, 10), (5, 6, 2), (6, 7, 1), (6, 8, 6), (7, 8, 7)]

adj = {i:[] for i in range(v)}

for x,y,w in arr:
    adj[x].append([w, y])
    adj[y].append([w, x])
    
weight = [float('inf') for i in range(v)]

weight[0] = 0

heap = [[0, 0]]

heapq.heapify(heap)

while len(heap) > 0:
    
    pw, parent = heapq.heappop(heap)
    
    for cw, child in adj[parent]:
        if weight[child] > cw + pw:
            weight[child] = cw + pw
            heapq.heappush(heap, [weight[child], child])
            
print(weight)
