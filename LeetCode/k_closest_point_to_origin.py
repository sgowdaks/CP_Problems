import collections

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dicti = {}
        dicti_count = {}
        for point in points:
            distance = sqrt(point[0]**2 + point[1]**2)
            p = (point[0], point[1])
            dicti[p] = distance
            if p not in dicti_count:
                dicti_count[p] = 1
            else:
                dicti_count[p] += 1
        
        dicti = dict(sorted(dicti.items(), key=lambda item: item[1]))
        
        result = []
        
        for key in dicti.keys():
            if k == 0:
                return result
            else:
                x, y = key[0], key[1]
                distance = [x, y]
                result.append(distance)
                k = k - 1
                if dicti_count[(x, y)] > 1:
                    count = dicti_count[(x, y)] - 1
                    while k > 0 and count > 0:
                        result.append(distance)
                        k = k - 1
                        count = count - 1
                        
        return result
                
            
        
