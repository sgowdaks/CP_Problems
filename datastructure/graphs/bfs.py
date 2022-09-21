#method 1
def bfsOfGraph(self, V, adj):
        list1 = []
        stack = []
        list1.append(0)
        stack.append(0)
        newl = [False] * V 
        while len(stack) > 0:
            k = stack.pop(0)
            newl[k] = True
            k = adj[k]
            for i in k:
                if newl[i] == False:
                    list1.append(i)
                    stack.append(i)
                    newl[i] = True
            
        return list1


#method2
class Solution:    
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):
        # code here
        answer = []
        stack = []
        stack.append(0)
        visited = [False] * V
        while len(stack) > 0:
            if visited[stack[0]] == False:
                k = stack.pop(0)
                visited[k] = True
                for i in adj[k]:
                    stack.append(i)
                answer.append(k)
            else:
                stack.pop(0)
        
        return answer
