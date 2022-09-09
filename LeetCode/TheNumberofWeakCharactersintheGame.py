class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        #with sorting
        properties.sort(key=lambda x:(-x[0],x[1]))
        print(properties)
        count = 0
        max_attack = properties[0][0]
        max_defence = properties[0][1]

        for i in range(1, len(properties)):
            if properties[i][0] < max_attack and properties[i][1] < max_defence:
                count = count + 1 
            else:
                max_attack = properties[i][0]
                max_defence = properties[i][1]

        return count
    
        #Brute force
#         count = 0
        
#         for i in range(len(properties)):
#             k = properties[i]
#             a = k[0]
#             d = k[1]
#             flag = 0
#             for j in range(0,len(properties)):
#                 if i == j:
#                     continue
#                 l = properties[j]
#                 if l[0] > a and l[1] > d:
#                     flag = 1
                    
#             if flag == 1:
#                 count = count + 1
                
#         return count
                    
                
            
         
        
