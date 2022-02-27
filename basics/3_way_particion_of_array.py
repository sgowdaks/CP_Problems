def threeWayPartition(self, arr, lowVal, highVal):
     #solution 1
	   # pointer = -1
	   # for i, val in enumerate(array):
	   #     if val >= a and pointer == -1:
	   #         pointer = i
	   #     elif val < a and pointer == -1:
	   #         pass
	   #     elif val < a and pointer != -1:
	   #         array[pointer], array[i] = array[i], array[pointer]
	   #         pointer = pointer + 1
	   #    # print(array)
	   # pointer = -1
	   ## print(array)
	   # for i, val in reversed(list(enumerate(array))):
	   #     if val <= b and pointer == -1:
	   #         pointer = i
	   #     elif val > b and pointer == -1:
	   #         pass
	   #     elif val > b and pointer != -1:
	   #         array[pointer], array[i] = array[i], array[pointer]
	   #         pointer = pointer - 1
	   ## print(array)
     #solution 2
	   start = 0
	   end = len(arr) - 1
	   i = 0
	   while start <= end:
	       if arr[start] < lowVal:
	           arr[start], arr[i] = arr[i], arr[start]
	           i = i + 1
	           start = start + 1
	       elif arr[start] > highVal:
	           arr[start], arr[end] = arr[end], arr[start]
	           end = end - 1
	       else:
	           start = start + 1
