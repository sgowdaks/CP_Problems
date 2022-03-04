def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        k = query_row
        query_row += 3
        list1 = [[0 for i in range(query_row)] for j in range(query_row)]
        # print(list1)
        list1[0][0] = poured
        # print(list1)
        for i in range(query_row-1):
            for j in range(0, i+1):
                # print(i,j)
                if list1[i][j] > 1:
                    # print(list1[i][j])
                    extra = (list1[i][j] - 1)/2
                    # print(extra)
                    list1[i][j] = 1
                    # print(list1[i][j])
                    list1[i+1][j] = list1[i+1][j] + extra
                    list1[i+1][j+1] = list1[i+1][j+1] + extra
                else:
                           pass
        if list1[k][query_glass] >= 1:
            return 1
        else:
            return list1[k][query_glass]
        return list1[k][query_glass]

                           
                    
                    
        
        
