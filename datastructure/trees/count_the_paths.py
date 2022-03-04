def possible_paths(self, edges, n, s, d):
        stack = []
        adjlist = {}
        if s == d:
            # print("k")
            if len(edges) == 0:
                # print("hello")
                return 1
        for e in range(n):
            ed = []
            for i,j in edges:
                if i == e:
                    ed.append(j)
            adjlist[e] = ed
        # print(adjlist)
        stack.append(s)
        count = 0
        count = self.dfs(stack, adjlist, s, d, n, count)
        if count == 0:
            if s == d:
                return 1
        return count
        
    def dfs(self,stack, adjlist, s, d, n, count):
        # print(stack)
        while len(stack) > 0:
            k = stack.pop()
            k = adjlist[k]
            # print(k)
            for i in k:
                if i == d:
                    # print("hello")
                    # print(i)
                    count += 1
                    return count
                else:
                    stack.append(i)
                    count = self.dfs(stack, adjlist, s, d, n, count)
        return count
                
            
            
