class Solution:
    def fourSum(self, arr: List[int], l: int) -> List[List[int]]:
        re = set()
        arr = sorted(arr)
        for i in range(len(arr)):
            num = l - arr[i]
            for j in range(i+1, len(arr)):
                num1 = num - arr[j]
                set_ = set()
                for k in range(j+1, len(arr)):
                    nums = num1 - arr[k]
                    if nums in set_:
                        re.add((arr[i], arr[j], arr[k], nums))
                    set_.add(arr[k])
                # print("hello")
        print(re)
        return re
