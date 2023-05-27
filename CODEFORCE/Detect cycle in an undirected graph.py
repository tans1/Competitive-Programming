from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		vis = [0] * V
        
        def dfs(node, parent):
            vis[node] = 1
            for adjNode in adj[node]:
                if vis[adjNode] == 0:
                    if dfs(adjNode, node):
                        return True
                elif adjNode != parent:
                    return True
            return False
        
        for i in range(V):
            if vis[i] == 0 and dfs(i, -1):
                return True
        return False
