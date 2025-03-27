class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        parent = [i for i in range(n)]
        rank = [1 for i in range(n)]

        def find(node):

            while node != parent[node]:
              #okay, why is this important? why can't it just be return parent[node] for simple senario it will work, but seanriors when the s
              #independed component the existed induvidually when it becomes part of bigger component, the small component child node, will have 
              #previous parent and not current/updated parents
                node = parent[node]
            return node

        for x, y in edges:
            xp = find(x)
            yp = find(y)

            print(xp, yp)

            if xp != yp:

                #they do not belong to same parent
                #the one with the highest rank should get the value

                if rank[xp] < rank[yp]:
                    yp, xp = xp, yp
                    #now xp will always have the highest rank
                
                parent[yp] = xp
                rank[xp] += 1

                n -= 1

        return n






        
        
