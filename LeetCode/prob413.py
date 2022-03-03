def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        arr = []
        arr.append(0)
        arr.append(0)
        if len(nums) < 3:
            return 0
        for i in range(2,len(nums)):
            if nums[i]-nums[i-1] == nums[i-1]-nums[i-2]:
                arr.append(1)
                arr[i] = arr[i-1] + arr[i]
            else:
                arr.append(0)
        return sum(arr)
