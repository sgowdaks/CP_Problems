class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        box = sorted(boxTypes, key = lambda x: -x[1])
        units = 0
        size = 0
        i = 0
        
        while i < len(boxTypes) and (size + box[i][0]) <= truckSize:
            k = box[i]
            val = box[i][0] * box[i][1]
            size += box[i][0]
            units += val
            i += 1
        
        if size < truckSize and i < len(boxTypes):
            units += (truckSize - size) * box[i][1]
        
        return units
