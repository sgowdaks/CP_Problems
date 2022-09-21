class Solution:
    
    #Function to return Breadth First Traversal of given graph.
    def dfsOfGraph(self, V, adj):
        # code here
        answer = []
        stack = []
        stack.append(0)
        visited = [False] * V
        
        def recurse(stack):
            if len(stack) == 0:
                return
            else:
                while len(stack) > 0:
                    if visited[stack[0]] == False:
                        k = stack.pop(0)
                        visited[k] = True
                        answer.append(k)
                        print(k, adj[k])
                        if len(adj[k]) == 0:
                            return
                        for i in adj[k]:
                            stack.append(i)
                            recurse(stack)
                    else:
                        stack.pop(0)
        recurse(stack)
        
        return answer
