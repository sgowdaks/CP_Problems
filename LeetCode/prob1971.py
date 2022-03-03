def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        
            
        adMat = defaultdict(list)
        for s, d in edges:
            adMat[s].append(d)
            adMat[d].append(s)
        # print(adMat)
        
        stack = []
        tabel = [False] * n
        # print(tabel)
        
        stack.append(source)
        # print(stack)
        while len(stack) > 0:
            k = stack.pop(0)
            tabel[k] = True
            k = adMat[k]
            # print(k)
            for i in k:
                if tabel[i] == False:
                    if i == destination:
                        return True
                    stack.append(i)
                    tabel[i] = True
                # print(tabel)
                # print(stack)
        return False
                    
