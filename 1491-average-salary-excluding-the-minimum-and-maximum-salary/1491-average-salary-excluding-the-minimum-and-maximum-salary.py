class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        n = len(salary) - 2
        return sum(salary[1:n+1]) / n
        