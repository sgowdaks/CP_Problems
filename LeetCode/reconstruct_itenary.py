class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(key=lambda x:(x[0],x[1]))
        dicti = defaultdict(list)
        answer = []
        
        #construct adjecent matrix
        for e, v in tickets:
            dicti[e].append(v)
        
        #backtracking algorithm
        result = ["JFK"]
        def dfs(src):
            if len(result) == len(tickets) + 1:
                return True
            if src not in dicti:
                return False

            for i in range(len(dicti[src])):
                res = dicti[src].pop(0)
                result.append(res)
                if dfs(res):
                    return True
                dicti[src].append(res)
                result.pop()
        
        
        dfs("JFK")
        return result
                
                
                
                
        
        
        
        
        
