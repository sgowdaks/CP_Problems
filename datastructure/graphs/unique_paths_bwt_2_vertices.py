def countPaths(self, V, adjlist , s, d):
        stack = []
        stack.append(s)
        count = 0
        count = self.dfs(stack, adjlist, s, d, count)
        if count == 0:
            if s == d:
                return 1
        return count
        
    def dfs(self,stack, adjlist, s, d, count):
        # print(stack)
        while len(stack) > 0:
            k = stack.pop()
            k = adjlist[k]
            # print(k)
            for i in k:
                if i == d:
                    count += 1
                    return count
                else:
                    stack.append(i)
                    count = self.dfs(stack, adjlist, s, d, count)
        return count
