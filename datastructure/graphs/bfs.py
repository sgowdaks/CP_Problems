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
