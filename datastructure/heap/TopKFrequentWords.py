#https://leetcode.com/problems/top-k-frequent-words/discuss/1657648/Simple-or-4-lines-or-using-heap-or-With-explanation
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dicti = {}
        for word in words:
            if word in dicti:
                dicti[word] += 1
            else:
                dicti[word] = 1
                
        heap = [(-value, key) for key, value in dicti.items()]
        
        heapq.heapify(heap)
        
        return [heapq.heappop(heap)[1] for _ in range(k)]
                
                
#         dicti = {}
#         for word in words:
#             if word in dicti:
#                 dicti[word] += 1
#             else:
#                 dicti[word] = 1
                
#         list1 = []
                
#         dicti = dict(sorted(dicti.items(), key=lambda item: item[0]))
#         dicti = dict(sorted(dicti.items(), key=lambda item: item[1], reverse = True))

#         count = 0
#         for key in dicti.keys():
#             if count == k:
#                 return list1
#             else:
#                 list1.append(key)
#                 count += 1
        
#         return list1
                
        

        
