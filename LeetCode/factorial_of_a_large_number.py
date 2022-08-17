class Solution:
    def factorial(self, N):
        arr =[]
        arr.append(1)
        if N == 1:
            return arr
        for i in range(2, N+1):
            reminder = 0
            for j in reversed(range(len(arr))):
                # print(i,j)
                total = (arr[j] * i) + reminder
                if total // 10 != 0:
                    arr[j] = total % 10
                    reminder = total // 10
                else:
                    arr[j] = total
                    reminder = 0
            # print(arr, reminder)
            if reminder != 0:
                arr.insert(0, reminder)
        return arr
