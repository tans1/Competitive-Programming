class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        temp = sorted(costs, key = lambda x: (x[0] - x[1]))
        forCityA =  temp[:len(temp) // 2]
        forCityB = temp[len(temp) // 2 : ]
        
        ans = 0
        for a,b in forCityA:
            ans += a
        
        for a,b in forCityB:
            ans += b
        
        return ans
        
        