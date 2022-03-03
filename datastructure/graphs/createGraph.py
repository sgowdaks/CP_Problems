class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.address = [None] * self.vertices
    
    def addEdge(self,start, end):
        node = Node(end)
        node.next = self.address[start]
        self.address[start] = node
        
        node = Node(start)
        node.next = self.address[end]
        self.address[end] = node
    
    def disAdjecent(self):
        for i, node in enumerate(self.address):
            char = ""
            print("Node at ",i)
            while node:
                print(node.data)
                node = node.next

                

V = 4
graph = Graph(V)
graph.addEdge(0,1)
graph.addEdge(0,2)
graph.addEdge(1,2)
graph.addEdge(1,3)
graph.addEdge(3,2)
graph.disAdjecent()
