        arr = []
        if N == 1:
            return str(1)
        while N > 1:
            if len(arr) == 0:
                arr = [int(i) for i in str(N)]
            else:
                carry = 0
                for i, e in reversed(list(enumerate(arr))):
                    # print(arr)
                    k = arr[i] * N + carry
                    # print(k)
                    carry = k // 10
                    k = k % 10
                    arr[i] = k
                if carry != 0:
                    arr.insert(0, carry)
            N = N - 1
        k = [str(i) for i in arr]
        l = "".join(k)
        return  l
