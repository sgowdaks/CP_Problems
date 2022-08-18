def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        right = 0
        left = 0
        count = 0
        product = 1
        
        if k <= 1:
            return 0
        
        while right < len(nums):
            product *= nums[right]
            # print(product)
            while product >= k:
                # print(product,k)
                product /= nums[left]
                left += 1
            # print(right,left)
            count += (right - left + 1)
        
            right += 1
        
        return count
