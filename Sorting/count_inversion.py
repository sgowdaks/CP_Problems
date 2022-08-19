def inversionCount(self, arr, n):
        def partician(arr):
            
            count = 0
            
            if len(arr) > 1:
                mid = len(arr) // 2
                left_arr = arr[:mid]
                right_arr = arr[mid:]
                
                count += partician(left_arr)
                count += partician(right_arr)
                
                i = j = k = 0
                
                # print("left: ", left_arr)
                # print("right: ", right_arr)
                
                while i < len(left_arr) and j < len(right_arr):
                    if left_arr[i] <= right_arr[j]:
                        arr[k] = left_arr[i]
                        i = i + 1
                    else:
                        count += len(left_arr) - i 
                        arr[k] = right_arr[j]
                        j = j + 1
                    k = k + 1
                
                while i < len(left_arr):
                    arr[k] = left_arr[i]
                    k = k+ 1
                    i = i + 1
                    
                while j < len(right_arr):
                    arr[k] = right_arr[j]
                    k = k+ 1
                    j = j + 1
                
            return count    
        
        return partician(arr)
