class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        #2pointer
        
        products = sorted(products)
        
        searchWord = list(searchWord)
        
        left = 0
        right = len(products) - 1
        
        list1 = []
        
        
        for i in range(len(searchWord)):
            # print(left, right)
            if i < len(products[left]) and searchWord[i] != products[left][i]:
                while left < right and searchWord[i] != products[left][i]:
                    left += 1
            if i >= len(products[left]): 
                while left < right:
                    if i < len(products[left]) and searchWord[i] == products[left][i]:
                        break
                    else:
                        left += 1
                
            if i < len(products[right]) and searchWord[i] != products[right][i]:
                while right > left and searchWord[i] != products[right][i]:
                    right -= 1
            if i >= len(products[right]): 
                while right > left:
                    print(j)
                    if i < len(products[right]) and searchWord[i] == products[right][i]:
                        break
                    else:
                        right -= 1

            if i < len(products[left]) and searchWord[i] == products[left][i] and searchWord[i] == products[right][i] and i < len(products[right]):
                if right - left >= 3:
                    k = products[left:left+3]
                    list1.append(k)
                else:
                    print(left, right+1)
                    list1.append(products[left:right+1])
            else:
                while i < len(searchWord):
                    list1.append([])
                    i += 1
                return list1
            
            
        return list1
            

                
                
                
        
        



            
            
            
            
            
        
            
            
        
        
        
        
        
