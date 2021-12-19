def containsDuplicate(self, nums: List[int]) -> bool:
        dicti = {}
        for i in nums:
            if i in dicti:
                return True
            else:
                dicti[i] = 1
        return False
