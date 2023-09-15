class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # it is Minimum Spanning tree : using kruskal algorithm
        parent = [-1 for _ in range(len(points))]
        ans = 0
        def find(u):
            root = u
            while root != parent[root] and parent[root] != -1:
                root = parent[root]
            while u != root:
                ancestor = parent[u]
                parent[u] = root
                u = ancestor
            return root
        def union(u,v,cost):
            nonlocal ans, parent
            rt1 = find(u)
            rt2 = find(v)
            if rt1 != rt2:
                ans += cost
                parent[rt2] = rt1

        nodes = []
        for i in range(len(points) - 1):
            for j in range(i+1,len(points)):
                manhattan_dst = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                nodes.append((i,j,manhattan_dst))

        nodes = sorted(nodes,key = lambda x: x[2])
        for u,v,cost in nodes:
            union(u,v,cost)
        return ans
        
        