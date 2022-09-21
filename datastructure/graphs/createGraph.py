#method 1
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


#method 2
class Graph:
    def __init__(self):
        self.dicti = {}
        
    #directed graph
    def directed_graph(self, start, end):
        if start not in self.dicti:
            self.dicti[start] = []
        if end not in self.dicti:
            self.dicti[end] = []
        
        self.dicti[start].append(end)
        
    #undirected graph
    def undirected_graph(self,start, end):
        if start not in self.dicti:
            self.dicti[start] = []
        if end not in self.dicti:
            self.dicti[end] = []
        
        self.dicti[start].append(end)
        self.dicti[end].append(start)
        
    def print_graph(self):
        for i in self.dicti.keys():
            for j in self.dicti[i]:
                print(i, "->", j)
 
graph = Graph()       
edges = input()
for i in range(int(edges)):
    node1, node2 = input().split()
    graph.directed_graph(node1, node2)

graph.print_graph()
    


