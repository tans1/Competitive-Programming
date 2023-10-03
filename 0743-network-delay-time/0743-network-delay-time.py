class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        
        for u,v,w in times:
            if u not in graph:
                graph[u] = []
            graph[u].append((v,w))
        
        # Dijskstra
        arr = [float("inf") for _ in range(n+1)]
        arr[k] = 0
        q = [(0,k)]
        
        while q:
            curr_weight, curr_node = heapq.heappop(q)  
            for nb, w in graph[curr_node]:
                if arr[nb] > curr_weight + w:
                    arr[nb] = curr_weight + w
                    heapq.heappush(q, (arr[nb], nb))
        
        mn = float("-inf")
        for num in arr[1:]:
            if num == float("inf"):
                return -1
            else:
                mn = max(mn, num)
        return mn
            