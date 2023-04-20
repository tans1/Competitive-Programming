class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for f,t in roads:
            graph[f].append(t)
            graph[t].append(f)
        
        srted = sorted(graph.items(), key = lambda x: -len(x[1]))
        
        ans = 0
        
        for i in range(len(srted)-1):
            for j in range(i+1, len(srted)):
                temp = len(srted[i][1]) + len(srted[j][1])
                
                if srted[i][0] in srted[j][1]:
                    temp -= 1
                
                ans = max(ans, temp)
        
        return ans