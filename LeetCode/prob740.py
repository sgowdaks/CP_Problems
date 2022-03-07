def deleteAndEarn(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums = sorted(nums)
        dicti = Counter(nums)
        max_ = [0] * len(dicti)
        keys = dicti.keys()
        keys_ = []
        for key in keys:
            keys_.append(key)
        print(keys_)
        max_[0] = keys_[0] * dicti[keys_[0]]
        for i, val in enumerate(keys_):
            if i == 0:
                pass
            else:
                if keys_[i] - keys_[i-1] == 1:
                    if i == 1:
                        max_[i] = keys_[i] * dicti[keys_[i]]
                    elif i == 2:
                        max_[i] = keys_[i] * dicti[keys_[i]] + max_[i-2]
                    else:
                        max_[i] = max(max_[i-2],max_[i-3])+ dicti[keys_[i]]*val
                else:
                     max_[i] = max(max_[i-1],max_[i-2])+ dicti[keys_[i]]*val
        # print(max_)
        return max(max_)
