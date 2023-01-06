class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        
        cnt = 0
        i = 0
        while i < len(costs) and coins >= costs[i]:
            cnt += 1
            coins -= costs[i]
            i += 1
        return cnt