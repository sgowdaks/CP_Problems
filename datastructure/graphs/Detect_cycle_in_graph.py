class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        helper = [False] * V
        visited = [False] * V
        for i in range(len(adj)):
            if visited[i] == False:
                if self.dfs(helper, visited, i, adj) == True:
                    return True
        return False
        
        
        
    def dfs(self, helper, visited, i, adj):
        helper[i] = True
        visited[i] = True
        for j in adj[i]:
            if visited[j] == False:
                if self.dfs(helper, visited, j, adj) == True:
                    return True
            elif helper[j] == True:
                return True
                
        helper[i] = False
        return False
