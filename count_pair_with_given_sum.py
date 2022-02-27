def getPairsCount(self, arr, n, k):
        # code here
        dicti= Counter(arr)
        count = 0
        for i, val in enumerate(arr):
            count += dicti[k - val]
            # print(count)
            if k-val == val:
                # print("hello")
                count = count - 1
        return count // 2
