class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        if len(points) == 1: return 1
        
        cnt = 0
        points = sorted(points, key=lambda x: x[0])
        prev = points[0]
        i = 1
        while i < len(points):
            if prev[1] >= points[i][0]:
                prev[0] = max(prev[0], points[i][0])
                prev[1] = min(prev[1], points[i][1])

            else:
                prev = points[i]
                cnt += 1

            i += 1
        
        return cnt+1