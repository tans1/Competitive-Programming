class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        grades.sort()
        cnt = 0
        i , j = 0, 0
        prevSum,prevNum = 0, 0
        while i < len(grades):
            curSum = 0
            while j - i + 1 <= prevNum and j < len(grades):
                curSum += grades[j]
                j += 1
            if j < len(grades) and j - i + 1 > prevNum and curSum + grades[j] > prevSum:
                prevSum = curSum + grades[j]
                prevNum = j - i + 1
                cnt += 1
                j += 1
            i = j
        return cnt
                
                
        