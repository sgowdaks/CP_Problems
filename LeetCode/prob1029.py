class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        list1 = []
        list2 = []
        for i, cost in enumerate(costs):
            list1.append(cost[1]-cost[0])
            list2.append(i)
        zipped = list(zip(list2, list1))
        res = sorted(zipped, key = lambda x: x[1])
        total = 0
        mid = len(costs) / 2
        k = 0
        for idx, val in res:
            # print(idx, val)
            if k < mid:
                total += costs[idx][1]
            else: 
                total += costs[idx][0]
            k = k + 1
        return total
