class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap = []
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                heapq.heappush(heap, [arr[i] / arr[j], arr[i], arr[j]])
        ans = heapq.nsmallest(k,heap)[-1]
        return [ans[1], ans[2]]
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    