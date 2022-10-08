class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr = sorted(arr)
        min_ = +10000000
        prev = arr[0]
        for i in range(1, len(arr)):
            min_ = min(min_, arr[i] - prev)
            prev = arr[i]
        
        main = []
        prev = arr[0]
        for i in range(1, len(arr)):
            k = arr[i] - prev
            if k == min_:
                main.append([prev, arr[i]])
            prev = arr[i]
        return main
