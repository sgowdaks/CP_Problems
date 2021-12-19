def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if m == 0:
            for i in range(n):
                nums1[m] = nums2[i]
                m = m + 1 
        else:
            k = m - 1
            #print(k)
            tmp = 0
            for i in range(n-1,-1,-1):
                k = m - 1
                if nums2[i] < nums1[k]:
                    #print("hello")
                    tmp = nums2[i]
                    nums2[i] = nums1[k]
                    nums1[k] = tmp
                    k = k - 1
                    #insertion sort
                    while k >= 0:
                        if nums1[k] > nums1[k+1]:
                            tmp1 = nums1[k]
                            nums1[k] = nums1[k+1]
                            nums1[k+1] = tmp1
                        elif nums1[k] < nums1[k+1]:
                            break
                        else:
                            break
                        k = k - 1 

            for i in range(n):
                nums1[m] = nums2[i]
                m = m + 1
                    
                  
