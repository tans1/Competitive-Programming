class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heapq.heappush(heap,matrix[i][j])
                j += 1

        ans = heapq.nsmallest(k,heap)
        return ans[-1]