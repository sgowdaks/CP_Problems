class MaxHeap:
 
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.heap = [0] * (self.maxsize)
        # self.heap[0] = 1000000
        self.first = 0
    
    def parent(self, pos):
        return (pos // 2)
        
    def get_high(self):
        # print(self.heap)
        self.heap[0] = self.heap[self.size]
        self.size = self.size - 1
        self.max_heapify(0)
    
    def isLeaf(self, pos):
         
        if pos >= (self.size//2) and pos <= self.size:
            return True
        return False
        
    
    def max_heapify(self, index):
        # print(index)
        if not self.isLeaf(index):
            left = index * 2 + 1
            right = index * 2 + 2
            
            if (self.heap[index] < self.heap[left] or
                self.heap[index] < self.heap[right]):
                    
                if (self.heap[left] > self.heap[right]):
                    self.heap[index], self.heap[left] = self.heap[left], self.heap[index]
                    # print(self.heap)
                    self.max_heapify(left)
                else:
                    self.heap[index], self.heap[right] = self.heap[right], self.heap[index]
                    # print(self.heap)
                    self.max_heapify(right)
                    
    
    def insert(self, element):
        if self.size > self.maxsize:
            return
        
        if self.size == 0 and self.first == 0:
            self.heap[self.size] = element
            self.first = 1
        else:    
        
            self.size += 1
            current = self.size
            self.heap[current] = element
        
            while self.heap[current] > self.heap[self.parent(current)]:
                self.heap[current], self.heap[self.parent(current)] = self.heap[self.parent(current)], self.heap[current]
                print(current, self.parent(current))
                print(self.heap[current], self.heap[self.parent(current)])
                current = self.parent(current)
    
    def Print(self):
        print(self.heap)
        
    
    
maxHeap = MaxHeap(15)
maxHeap.insert(5)
maxHeap.insert(3)
maxHeap.insert(17)
maxHeap.insert(10)
maxHeap.insert(84)
maxHeap.insert(19)
maxHeap.insert(6)
maxHeap.insert(22)
maxHeap.insert(9)
maxHeap.Print()
maxHeap.get_high()
maxHeap.Print()



