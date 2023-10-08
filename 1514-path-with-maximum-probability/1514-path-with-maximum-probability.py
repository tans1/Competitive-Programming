class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = {}
        for i in range(len(edges)):
            u,v = edges[i][0], edges[i][1]
            w = succProb[i]
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
                
            graph[u].append((v,w))
            graph[v].append((u,w))
        
            
        dist = [float("-inf") for _ in range(n)]
        dist[start_node] = 1
        
        q = [(-1,start_node)]
        
        visited = set()
        while q:
            curr_prop , node = heapq.heappop(q)
            
            if node in visited:
                continue
            visited.add(node)
            
            for v,w in graph.get(node,[]):
                if dist[node]*w > dist[v]:
                    dist[v] = max(dist[node]*w , dist[v])
                    heapq.heappush(q, (-1 * dist[node]*w , v))
        
        if dist[end_node] != float("-inf"):
            return dist[end_node]
        return 0
            
            