class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for i in range(len(points)):
            heapq.heappush(h, ((points[i][0] * points[i][0]) + (points[i][1] * points[i][1]) , i))
        min_ = heapq.nsmallest(k, h)
        ans = []
        for key, index in min_:
            ans.append(points[index])
        return ans
            