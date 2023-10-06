class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        srted = sorted(costs, key = lambda x: (x[0]-x[1]))
        cityA , cityB = 0,0
        for i in range(len(costs) // 2):
            cityA += srted[i][0]
            cityB += srted[len(costs) - i -1][1]
        return  cityA + cityB
        
        