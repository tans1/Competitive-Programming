class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,w in flights:
            graph[u].append((v,w))
        
        dist = [float("inf") for _ in range(n)]
        dist[src] = 0
        ans = float("inf")
        q = [(0,src,k)]
        visited = set()
        
        while q:
            curr_weight, curr_node, curr_stop = heapq.heappop(q)
            
            # print(curr_weight, curr_node, curr_stop)
            if curr_node == dst and curr_stop >= -1 :
                ans = min(ans, curr_weight)
                

            if (curr_node,curr_stop) in visited:
                continue
            visited.add((curr_node,curr_stop))
            
            
            for nb in graph[curr_node]:
                if curr_stop >= 0 and curr_weight + nb[1] < dist[nb[0]]:
                    heapq.heappush(q,(curr_weight + nb[1], nb[0], curr_stop - 1))
                    # dist[nb[0]] = curr_weight + nb[1]
                    
        
        # print(dist)
        if ans == float("inf"):
            return -1
        return ans