class Node:
    def __init__(self, value, row, col):
        self.value = value
        self.row = row
        self.col = col

class MaxHeap:
 
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.heap = [0] * (self.maxsize)
        self.first = 0
    
    def parent(self, pos):
        return (pos // 2)
        
    def get_high(self):
        # print(self.heap)
        k = self.heap[0]
        self.heap[0] = self.heap[self.size]
        self.size = self.size - 1
        self.max_heapify(0)
        return k
    
    def isLeaf(self, pos):
         
        if pos >= (self.size//2) and pos <= self.size:
            return True
        return False
        
    
    def max_heapify(self, index):
        # print(index)
        if not self.isLeaf(index):
            left = index * 2 + 1
            right = index * 2 + 2
            
            if (self.heap[index].value > self.heap[left].value or
                self.heap[index].value > self.heap[right].value):
                    
                if (self.heap[left].value < self.heap[right].value):
                    self.heap[index], self.heap[left] = self.heap[left], self.heap[index]
                    # print(self.heap)
                    self.max_heapify(left)
                else:
                    self.heap[index], self.heap[right] = self.heap[right], self.heap[index]
                    # print(self.heap)
                    self.max_heapify(right)
                    
    
    def insert(self, element, row, col):
        if self.size > self.maxsize:
            return
        
        if self.size == 0 and self.first == 0:
            self.heap[self.size] = Node(element, row, col)
            self.first = 1
        else:    
        
            self.size += 1
            current = self.size
            self.heap[current] = Node(element, row, col)
        
            while self.heap[current].value < self.heap[self.parent(current)].value:
                self.heap[current], self.heap[self.parent(current)] = self.heap[self.parent(current)], self.heap[current]
                current = self.parent(current)
    
    def Print(self):
        list1 = []
        for i in range(self.size+1):
            list1.append(self.heap[i].value)
        print(list1)
        
    

mat = [[10, 20, 30, 90],
        [15, 25, 35, 95],
        [27, 29, 39, 100],
        [32, 33, 39, 101]]
    
maxHeap = MaxHeap(len(mat))
for i in range(len(mat)):
    maxHeap.insert(mat[i][0], i , 0)
maxHeap.Print()



answer = []

for count in range(len(mat)*len(mat[0])):
    k = maxHeap.get_high()
    answer.append(k.value)
    row = k.row
    col = k.col
    if col + 1 < len(mat[0]):
        # print("hello")
        maxHeap.insert(mat[row][col+1], row , col+1)
    else:
        maxHeap.insert(10000, -1 , -1)
print(answer)


