class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        dct = defaultdict(list)
        for u,v in edges:
            dct[u].append(v)
            dct[v].append(u)
        
        def dfs(cur,par): 
            temp = 0    
            for nb in dct[cur]:
                if nb == par:
                    continue
                temp2 = dfs(nb,cur)
                if temp2 > 0 or hasApple[nb]:
                    temp += 2 + temp2
            return temp
        
        return dfs(0,-1)