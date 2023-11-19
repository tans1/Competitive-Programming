class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        years = [0 for i in range(2051)]
        for i,j in logs:
            years[i] += 1
            years[j] -= 1
        for i in range(1,len(years)):
            years[i] += years[i-1]
        mx = max(years)
        return years.index(mx)