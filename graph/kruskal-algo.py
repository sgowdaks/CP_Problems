#kruskals algorithm on graph
edges = [[0, 1, 10], [0, 2, 6],[0, 3, 5], [1, 3, 15], [2, 3, 4]]
n = 4

#find minimum spanning tree 
#kruskals === union find algorithm

#sort based on height and add it to heap, and remove those elemnt from heap with smallest value

import heapq

class Unifind:
    
    def __init__(self, n):
        self.node = n
        self.rank = [1] * n
        self.parent = [i for i in range(n)]
        
    def find(self, val):
        
        while self.parent[val] != val:
            self.parent[val] = self.parent[self.parent[val]]
            val = self.parent[val]
        return self.parent[val]
        
    def union(self, x, y):
        
        xp = self.find(x)
        yp = self.find(y)
        
        if xp == yp:
            #x and y parents are same
            return False
        
        if self.rank[xp] < self.rank[yp]:
            #xp is always higher
            xp, yp = yp, xp
            
        self.rank[xp] += self.parent[yp]
        self.parent[yp] = xp
    
        return True
      

heap = []

for x, y, weight in edges:
    heap.append([weight, x, y])
    
heapq.heapify(heap)

uf = Unifind(n)

total = 0

while len(heap) > 0:
    weight, x, y = heapq.heappop(heap)
    if uf.union(x, y):
        total += weight
        
print("Total: ", total)
        
        
    




